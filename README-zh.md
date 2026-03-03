# CS146S：现代软件工程师作业

这里是 [CS146S：现代软件工程师](https://themodernsoftware.dev) 课程的作业主页，该课程于 2025 年秋季在斯坦福大学开设。

## 仓库设置

这些步骤适用于 Python 3.12。

1. 安装 Anaconda
   - 下载并安装：[Anaconda 个人版](https://www.anaconda.com/download)
   - 打开新终端，使 `conda` 在你的 `PATH` 中

2. 创建并激活 Conda 环境（Python 3.12）
   ```bash
   conda create -n cs146s python=3.12 -y
   conda activate cs146s
   ```

3. 安装 Poetry
   ```bash
   curl -sSL https://install.python-poetry.org | python -
   ```

4. 使用 Poetry 安装项目依赖（在激活的 Conda 环境中）
   从仓库根目录运行：
   ```bash
   poetry install --no-interaction
   ```
