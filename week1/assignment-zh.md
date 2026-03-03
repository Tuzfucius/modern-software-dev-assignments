# 第一周 — 提示词技巧

你将通过制作提示词来完成特定任务，从而练习多种提示词技巧。每个任务的说明位于对应源文件的顶部。

## 安装

请先完成顶层 `README.md` 中描述的安装步骤。

## Ollama 安装

我们将使用一个名为 [Ollama](https://ollama.com/) 的工具来在本地机器上运行不同的前沿 LLM。使用以下方法之一：

- macOS（Homebrew）：
  ```bash
  brew install --cask ollama
  ollama serve
  ```

- Linux（推荐）：
  ```bash
  curl -fsSL https://ollama.com/install.sh | sh
  ```

- Windows：
  从 [ollama.com/download](https://ollama.com/download) 下载并运行安装程序。

验证安装：
```bash
ollama -v
```

在运行测试脚本之前，请确保已下载以下模型。只需执行一次（除非以后删除模型）：
```bash
ollama run mistral-nemo:12b
ollama run llama3.1:8b
```

## 技巧和源文件
- K-shot 提示 — `week1/k_shot_prompting.py`
- 思维链 — `week1/chain_of_thought.py`
- 工具调用 — `week1/tool_calling.py`
- 自洽性提示 — `week1/self_consistency_prompting.py`
- RAG（检索增强生成）— `week1/rag.py`
- 反思 — `week1/reflexion.py`

## 交付物
- 阅读每个文件中的任务描述。
- 设计和运行提示词（查找代码中所有标有 `TODO` 的地方）。这应该是你唯一需要更改的内容（即不要调整模型参数）。
- 迭代改进结果，直到测试脚本通过。
- 为每种技巧保存最终的提示词和输出。
- 确保在提交中包含每个提示词技巧文件的完成代码。***仔细检查所有 `TODO` 是否已解决。***

## 评估标准（60 分满分）
- 每完成一种提示技巧得 10 分，共 6 种技巧
