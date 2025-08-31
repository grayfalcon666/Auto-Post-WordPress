# WordPress 文章发布工具与 AI 排版优化

这个项目包含两个主要组件：一个 WordPress 文章发布工具和一个 AI 排版优化模块，两者可以协同工作，帮助用户创建和优化博客内容。

## 项目结构

```
wordpress-ai-publisher/
├── main.py                 # 主程序 - WordPress 文章发布工具
├── ai_formatter.py         # AI 排版优化模块
├── config.py               # 配置文件（可选）
├── requirements.txt        # 项目依赖
└── README.md              # 项目说明文档
```

## 功能特点

### WordPress 文章发布工具 (`main.py`)
- ✨ 通过 WordPress REST API 发布文章
- 🎨 支持手动输入 HTML 格式内容
- 📝 灵活的输入方式，使用 `:END` 标记结束输入
- 🔧 可设置文章状态（发布/草稿）
- 🏷️ 支持分类和标签设置
- 📋 提供文章摘要功能
- ✅ 发布前确认机制，避免误操作

### AI 排版优化模块 (`ai_formatter.py`)
- 🤖 集成 OpenAI GPT 模型进行内容优化
- 🎛️ 可配置的 AI 参数（温度、最大 token 数等）
- 📝 自定义提示词模板系统
- ⚙️ 用户可调整优化强度和质量
- 🔄 支持多轮优化和预览

## 安装与配置

### 环境要求

- Python 3.6+
- WordPress 5.6+ (支持应用程序密码功能)
- OpenAI API 账户和 API 密钥

### 安装步骤

1. 克隆或下载此项目到本地
2. 安装必要的 Python 依赖：
   ```bash
   pip install -r requirements.txt
   ```
   或手动安装：
   ```bash
   pip install requests openai
   ```
3. 配置 OpenAI API 密钥：
   ```bash
   export OPENAI_API_KEY='你的OpenAI API密钥'
   ```
   或在代码中直接设置（不推荐，因为安全性较低）

4. 在 WordPress 后台生成应用程序密码：
   - 进入「用户」→「个人资料」
   - 在「应用程序密码」部分创建新密码
   - 复制并保存生成的密码

## 使用方法

### 基本使用

1. 运行主程序：
   ```bash
   python main.py
   ```

2. 按照提示输入文章内容和其他信息

3. 当询问是否使用 AI 排版优化时，选择 'y' 或 'n'

4. 如果选择使用 AI 优化，按照提示配置优化参数

5. 确认发布信息后，文章将被发送到 WordPress

### AI 排版优化配置

当选择使用 AI 排版优化时，程序会提供以下配置选项：

1. **提示词模板**：选择或自定义用于指导 AI 优化的提示词
2. **温度参数**：控制 AI 创造性的参数（0.0-1.0，默认 0.7）
3. **最大 token 数**：限制 AI 响应的长度
4. **优化强度**：控制优化程度的参数

### 自定义提示词模板

您可以通过编辑 `ai_formatter.py` 中的 `PROMPT_TEMPLATES` 字典来自定义提示词模板：

```python
PROMPT_TEMPLATES = {
    "default": "请优化以下内容的排版，使其更易读和专业：\n\n{}",
    "technical": "作为技术文档专家，请优化以下技术内容的排版：\n\n{}",
    "creative": "请以创意写作的方式优化以下内容，使其更生动有趣：\n\n{}",
    # 添加您自己的模板...
}
```

## 配置选项

### OpenAI 参数配置

在 `ai_formatter.py` 中，您可以调整以下 OpenAI 参数：

```python
# OpenAI 参数默认值
DEFAULT_TEMPERATURE = 0.7
DEFAULT_MAX_TOKENS = 1000
DEFAULT_MODEL = "gpt-3.5-turbo"
```

### WordPress 参数配置

在 `main.py` 中，您可以设置默认的 WordPress 配置：

```python
# 默认配置
DEFAULT_SITE_URL = "https://yourwordpresssite.com"
DEFAULT_USERNAME = "your_username"
DEFAULT_APP_PASSWORD = "your_app_password"
```

## 高级用法

### 单独使用 AI 排版优化模块

您可以单独使用 `ai_formatter.py` 模块来优化任何文本内容：

```python
from ai_formatter import optimize_content

# 优化内容
original_content = "您的原始内容..."
optimized_content = optimize_content(
    original_content,
    prompt_template="default",
    temperature=0.7,
    max_tokens=1000
)

print(f"优化前: {original_content}")
print(f"优化后: {optimized_content}")
```

### 批量处理文章

您可以修改主程序以支持批量处理多篇文章：

```python
# 示例批量处理代码
articles = [
    {"title": "文章1", "content": "内容1..."},
    {"title": "文章2", "content": "内容2..."},
    # 更多文章...
]

for article in articles:
    # 应用 AI 优化
    if use_ai_optimization:
        article["content"] = optimize_content(article["content"])
    
    # 发布到 WordPress
    result = publisher.create_html_post(
        title=article["title"],
        html_content=article["content"],
        status=status
    )
```

## 故障排除

### 常见问题

1. **OpenAI API 错误**
   - 检查 API 密钥是否正确设置
   - 确认 API 密钥有足够的余额

2. **WordPress 连接问题**
   - 检查站点 URL、用户名和应用程序密码是否正确
   - 确认 WordPress REST API 已启用

3. **AI 优化效果不理想**
   - 尝试调整温度参数
   - 修改或自定义提示词模板

### 获取帮助

如果您遇到问题，可以：

1. 检查控制台输出的错误信息
2. 确保所有依赖项已正确安装
3. 确认 API 密钥和 WordPress 凭据正确

## 贡献指南

欢迎为这个项目做出贡献！您可以通过以下方式参与：

1. 报告 bug 或提出新功能建议
2. 提交 Pull Request 改进代码
3. 添加新的提示词模板
4. 改进文档

## 许可证

本项目采用 MIT 许可证。详见 [LICENSE](LICENSE) 文件。

## 更新日志

### v1.1.0 (2025-08-31)
- 新增 AI 排版优化模块
- 添加可配置的 OpenAI 参数
- 实现自定义提示词模板系统
- 添加优化强度控制选项

### v1.0.0 (2025-09-01)
- 初始版本发布
- 支持手动输入 HTML 内容
- 支持设置文章状态、分类、标签和摘要
- 添加发布前确认机制

---

如有问题或建议，请通过 Issue 反馈或联系开发者。