import ast
import json
import os
from typing import Any, Dict, List, Optional, Tuple, Callable

from dotenv import load_dotenv
from ollama import chat

load_dotenv()

NUM_RUNS_TIMES = 3


# ==========================
# 工具实现（"执行器"）
# ==========================
def _annotation_to_str(annotation: Optional[ast.AST]) -> str:
    if annotation is None:
        return "None"
    try:
        return ast.unparse(annotation)  # type: ignore[attr-defined]
    except Exception:
        # 尽力而为的后备方案
        if isinstance(annotation, ast.Name):
            return annotation.id
        return type(annotation).__name__


def _list_function_return_types(file_path: str) -> List[Tuple[str, str]]:
    with open(file_path, "r", encoding="utf-8") as f:
        source = f.read()
    tree = ast.parse(source)
    results: List[Tuple[str, str]] = []
    for node in tree.body:
        if isinstance(node, ast.FunctionDef):
            return_str = _annotation_to_str(node.returns)
            results.append((node.name, return_str))
    # 排序以获得稳定的输出
    results.sort(key=lambda x: x[0])
    return results


def output_every_func_return_type(file_path: str = None) -> str:
    """工具：返回每个顶层函数的 "name: return_type" 列表，以换行分隔。"""
    path = file_path or __file__
    if not os.path.isabs(path):
        # 如果不是绝对路径，尝试相对于此脚本的文件
        candidate = os.path.join(os.path.dirname(__file__), path)
        if os.path.exists(candidate):
            path = candidate
    pairs = _list_function_return_types(path)
    return "\n".join(f"{name}: {ret}" for name, ret in pairs)


# 示例函数，确保有内容可以分析
def add(a: int, b: int) -> int:
    return a + b


def greet(name: str) -> str:
    return f"Hello, {name}!"

# 用于按名称动态执行的工具注册表
TOOL_REGISTRY: Dict[str, Callable[..., str]] = {
    "output_every_func_return_type": output_every_func_return_type,
}

# ==========================
# 提示词脚手架
# ==========================

# TODO: 请填写此处！
YOUR_SYSTEM_PROMPT = ""


def resolve_path(p: str) -> str:
    if os.path.isabs(p):
        return p
    here = os.path.dirname(__file__)
    c1 = os.path.join(here, p)
    if os.path.exists(c1):
        return c1
    # 如需要，尝试项目根目录的同级目录
    return p


def extract_tool_call(text: str) -> Dict[str, Any]:
    """从模型输出中解析单个 JSON 对象。"""
    text = text.strip()
    # 某些模型将 JSON 包裹在代码围栏中；尝试去除
    if text.startswith("```") and text.endswith("```"):
        text = text.strip("`")
        if text.lower().startswith("json\n"):
            text = text[5:]
    try:
        obj = json.loads(text)
        return obj
    except json.JSONDecodeError:
        raise ValueError("模型未返回有效的工具调用 JSON")


def run_model_for_tool_call(system_prompt: str) -> Dict[str, Any]:
    response = chat(
        model="llama3.1:8b",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": "请调用工具。"},
        ],
        options={"temperature": 0.3},
    )
    content = response.message.content
    return extract_tool_call(content)


def execute_tool_call(call: Dict[str, Any]) -> str:
    name = call.get("tool")
    if not isinstance(name, str):
        raise ValueError("工具调用 JSON 缺少 'tool' 字符串")
    func = TOOL_REGISTRY.get(name)
    if func is None:
        raise ValueError(f"未知工具：{name}")
    args = call.get("args", {})
    if not isinstance(args, dict):
        raise ValueError("工具调用 JSON 的 'args' 必须是对象")

    # 如果存在 file_path 参数，尽力解析路径
    if "file_path" in args and isinstance(args["file_path"], str):
        args["file_path"] = resolve_path(args["file_path"]) if str(args["file_path"]) != "" else __file__
    elif "file_path" not in args:
        # 为期望 file_path 的工具提供默认值
        args["file_path"] = __file__

    return func(**args)


def compute_expected_output() -> str:
    # 基于实际文件内容的真实预期输出
    return output_every_func_return_type(__file__)


def test_your_prompt(system_prompt: str) -> bool:
    """运行一次：要求模型生成有效的工具调用；将工具输出与预期进行比较。"""
    expected = compute_expected_output()
    for _ in range(NUM_RUNS_TIMES):
        try:
            call = run_model_for_tool_call(system_prompt)
        except Exception as exc:
            print(f"解析工具调用失败：{exc}")
            continue
        print(call)
        try:
            actual = execute_tool_call(call)
        except Exception as exc:
            print(f"工具执行失败：{exc}")
            continue
        if actual.strip() == expected.strip():
            print(f"生成的工具调用：{call}")
            print(f"生成的输出：{actual}")
            print("成功")
            return True
        else:
            print("预期输出：\n" + expected)
            print("实际输出：\n" + actual)
    return False


if __name__ == "__main__":
    test_your_prompt(YOUR_SYSTEM_PROMPT)
