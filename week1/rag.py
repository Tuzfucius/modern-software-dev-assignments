import os
import re
from typing import List, Callable
from dotenv import load_dotenv
from ollama import chat

load_dotenv()

NUM_RUNS_TIMES = 5

DATA_FILES: List[str] = [
    os.path.join(os.path.dirname(__file__), "data", "api_docs.txt"),
]


def load_corpus_from_files(paths: List[str]) -> List[str]:
    corpus: List[str] = []
    for p in paths:
        if os.path.exists(p):
            try:
                with open(p, "r", encoding="utf-8") as f:
                    corpus.append(f.read())
            except Exception as exc:
                corpus.append(f"[load_error] {p}: {exc}")
        else:
            corpus.append(f"[missing_file] {p}")
    return corpus


# 从外部文件加载语料库（简单的 API 文档）。如果缺失，则回退到内联代码片段
CORPUS: List[str] = load_corpus_from_files(DATA_FILES)

QUESTION = (
    "编写一个 Python 函数 `fetch_user_name(user_id: str, api_key: str) -> str`，该函数调用文档化的 API "
    "根据 id 获取用户，并仅将用户名作为字符串返回。"
)


# TODO: 请填写此处！
YOUR_SYSTEM_PROMPT = ""


# 对于这个简单的例子
# 对于这个编码任务，通过必需的代码片段而不是精确字符串来验证
REQUIRED_SNIPPETS = [
    "def fetch_user_name(",
    "requests.get",
    "/users/",
    "X-API-Key",
    "return",
]


def YOUR_CONTEXT_PROVIDER(corpus: List[str]) -> List[str]:
    """为任务从 CORPUS 中选择并返回相关的文档子集。"""
    # 模拟简单的检索逻辑：寻找包含 API 参考信息的文档
    return [doc for doc in corpus if "API Reference" in doc]


def make_user_prompt(question: str, context_docs: List[str]) -> str:
    if context_docs:
        context_block = "\n".join(f"- {d}" for d in context_docs)
    else:
        context_block = "(未提供上下文)"
    return (
        f"上下文（仅使用此信息）：\n{context_block}\n\n"
        f"任务：{question}\n\n"
        "要求：\n"
        "- 使用文档化的基础 URL 和端点。\n"
        "- 发送文档化的认证头。\n"
        "- 对非 200 响应抛出异常。\n"
        "- 仅返回用户名字符串。\n\n"
        "输出：一个包含函数和必要导入的单一 Python 代码块。\n"
    )


def extract_code_block(text: str) -> str:
    """提取最后一个带围栏的 Python 代码块，或任意带围栏的代码块，否则返回原文。"""
    # 首先尝试 ```python ... ```
    m = re.findall(r"```python\n([\s\S]*?)```", text, flags=re.IGNORECASE)
    if m:
        return m[-1].strip()
    # 回退到任意带围栏的代码块
    m = re.findall(r"```\n([\s\S]*?)```", text)
    if m:
        return m[-1].strip()
    return text.strip()


def test_your_prompt(system_prompt: str, context_provider: Callable[[List[str]], List[str]]) -> bool:
    """运行最多 NUM_RUNS_TIMES 次，如果任何输出匹配 EXPECTED_OUTPUT 则返回 True。"""
    context_docs = context_provider(CORPUS)
    user_prompt = make_user_prompt(QUESTION, context_docs)

    for idx in range(NUM_RUNS_TIMES):
        print(f"Running test {idx + 1} of {NUM_RUNS_TIMES}")
        response = chat(
            model="llama3.1:8b",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt},
            ],
            options={"temperature": 0.0},
        )
        output_text = response.message.content
        code = extract_code_block(output_text)
        missing = [s for s in REQUIRED_SNIPPETS if s not in code]
        if not missing:
            print(output_text)
            print("SUCCESS")
            return True
        else:
            print("Missing required snippets:")
            for s in missing:
                print(f"  - {s}")
            print("Generated code:\n" + code)
    return False


if __name__ == "__main__":
    test_your_prompt(YOUR_SYSTEM_PROMPT, YOUR_CONTEXT_PROVIDER)
