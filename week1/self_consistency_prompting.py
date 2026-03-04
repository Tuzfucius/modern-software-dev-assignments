import os
import re
from collections import Counter
from dotenv import load_dotenv
from ollama import chat

load_dotenv()

NUM_RUNS_TIMES = 5

# TODO: 请填写此处！尝试在所有运行中达到接近 100% 的正确率。
YOUR_SYSTEM_PROMPT = ""

USER_PROMPT = """
解答此问题，然后在最后一行给出最终答案，格式为 "Answer: <number>"。

Henry 在他的 60 英里自行车旅行中停了两次。他第一次在 20 英里后停车。
第二次停车是在离终点前 15 英里处。他在第一次和第二次停车之间骑行了多少英里？
"""

EXPECTED_OUTPUT = "Answer: 25"


def extract_final_answer(text: str) -> str:
    """从详细的推理过程中提取最后的 'Answer: ...' 行。

    - 查找以 'Answer:' 开头的最后一行（不区分大小写）
    - 当存在数字时，将其规范化为 'Answer: <number>'
    - 如果未检测到数字，则返回匹配的内容作为后备
    """
    matches = re.findall(r"(?mi)^\s*answer\s*:\s*(.+)\s*$", text)
    if matches:
        value = matches[-1].strip()
        num_match = re.search(r"-?\d+(?:\.\d+)?", value.replace(",", ""))
        if num_match:
            return f"Answer: {num_match.group(0)}"
        return f"Answer: {value}"
    return text.strip()


def test_your_prompt(system_prompt: str) -> bool:
    """运行提示词 NUM_RUNS_TIMES 次，对提取的 'Answer: ...' 行进行多数投票。

    如果多数答案等于 EXPECTED_OUTPUT，则打印 "SUCCESS"。
    """
    answers: list[str] = []
    for idx in range(NUM_RUNS_TIMES):
        print(f"运行测试 {idx + 1}/{NUM_RUNS_TIMES}")
        response = chat(
            model="llama3.1:8b",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": USER_PROMPT},
            ],
            options={"temperature": 1},
        )
        output_text = response.message.content
        final_answer = extract_final_answer(output_text)
        print(f"第 {idx + 1} 次运行答案：{final_answer}")
        answers.append(final_answer.strip())

    if not answers:
        print("未产生任何答案。")
        return False

    counts = Counter(answers)
    majority_answer, majority_count = counts.most_common(1)[0]
    print(f"多数答案：{majority_answer} ({majority_count}/{len(answers)})")

    if majority_answer.strip() == EXPECTED_OUTPUT.strip():
        print("成功")
        return True

    # 当多数答案与预期不符时，打印分布用于调试
    print(f"预期输出：{EXPECTED_OUTPUT}")
    print("答案分布：")
    for answer, count in counts.most_common():
        print(f"  {answer}: {count}")
    return False


if __name__ == "__main__":
    test_your_prompt(YOUR_SYSTEM_PROMPT)


