# WordPress 文章发布工具与 AI 排版优化

一个通过 WordPress REST API 自动发布文章并集成 AI 排版优化功能的 Python 工具，支持 HTML 内容输入和 AI 辅助内容优化。

## ✨ 功能特点

- **WordPress 文章发布**：通过 REST API 自动发布文章到 WordPress
- **HTML 内容支持**：支持手动输入 HTML 格式内容
- **AI 排版优化**：集成 OpenAI GPT 模型进行内容优化和排版
- **灵活配置**：所有配置集中管理，支持自定义提示词模板
- **交互式界面**：用户友好的命令行交互界面
- **错误处理**：完善的错误处理和用户提示

## 📁 项目结构

```
wordpress-ai-publisher/
├── main.py                 # 主程序 - WordPress 文章发布工具
├── ai_formatter.py         # AI 排版优化模块
├── config.py               # 集中配置文件
├── requirements.txt        # 项目依赖
└── README.md              # 项目说明文档
```

## 🛠️ 安装与配置

### 环境要求

- Python 3.6+
- WordPress 5.6+ (支持应用程序密码功能)
- OpenAI API 账户

### 安装步骤

1. 克隆或下载此项目到本地
2. 安装必要的 Python 依赖：
   ```bash
   pip install -r requirements.txt
   ```
3. 配置 `config.py` 文件：
   - 设置 WordPress 站点 URL、用户名和应用程序密码
   - 配置 OpenAI API 密钥和其他参数
4. 在 WordPress 后台生成应用程序密码：
   - 进入「用户」→「个人资料」
   - 在「应用程序密码」部分创建新密码
   - 复制并保存生成的密码

## ⚙️ 配置说明

编辑 `config.py` 文件进行配置：

### WordPress 配置
```python
WORDPRESS = {
    "SITE_URL": "https://yourwordpresssite.com",  # 你的WordPress站点地址
    "USERNAME": "your_username",               # 你的WordPress用户名
    "APP_PASSWORD": "your_app_password",       # 你的应用程序密码
}
```

### OpenAI 配置
```python
OPENAI = {
    "API_KEY": "your_openai_api_key",          # 你的OpenAI API密钥
    "BASE_URL": "https://api.openai.com/v1",   # OpenAI API基础URL
    "DEFAULT_MODEL": "gpt-3.5-turbo",          # 默认模型
    "DEFAULT_TEMPERATURE": 0.7,                # 默认温度参数 (0.0-1.0)
    "DEFAULT_MAX_TOKENS": 1000,                # 默认最大token数
}
```

### 提示词模板配置
```python
PROMPT_TEMPLATES = {
    "default": "请优化以下内容的排版，使其更易读和专业：\n\n{}",
    "technical": "作为技术文档专家，请优化以下技术内容的排版：\n\n{}",
    "creative": "请以创意写作的方式优化以下内容，使其更生动有趣：\n\n{}",
    # 添加您自己的模板...
}
```

## 🚀 使用方法

### 基本使用

1. 运行主程序：
   ```bash
   python main.py
   ```

2. 按照提示输入：
   - 文章标题
   - HTML 内容（输入完成后输入 `:END` 结束）
   - 是否使用 AI 排版优化
   - 发布状态（发布/草稿）
   - 分类和标签 ID（可选）
   - 文章摘要（可选）

3. 确认发布信息后，文章将被发送到 WordPress

### AI 排版优化

当选择使用 AI 排版优化时，程序会提供以下配置选项：

1. **提示词模板**：选择或自定义用于指导 AI 优化的提示词
2. **温度参数**：控制 AI 创造性的参数（0.0-1.0，默认 0.7）
3. **最大 token 数**：限制 AI 响应的长度

## 🔧 高级用法

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

### 自定义提示词模板

您可以通过编辑 `config.py` 中的 `PROMPT_TEMPLATES` 字典来自定义提示词模板：

```python
PROMPT_TEMPLATES = {
    "default": "请优化以下内容的排版，使其更易读和专业：\n\n{}",
    "technical": "作为技术文档专家，请优化以下技术内容的排版：\n\n{}",
    "creative": "请以创意写作的方式优化以下内容，使其更生动有趣：\n\n{}",
    # 添加您自己的模板...
}
```

## 🐛 故障排除

### 常见问题

1. **OpenAI API 错误**
   - 确保 API 密钥正确设置
   - 确认 API 密钥有足够的余额
   - **注意**: 此项目使用 OpenAI Python 库 0.27.4 版本，新版本可能存在兼容性问题

2. **WordPress 连接问题**
   - 检查站点 URL、用户名和应用程序密码是否正确
   - 确认 WordPress REST API 已启用
   - 确保用户有发布文章的权限

3. **401 未授权错误**
   - 检查应用程序密码是否正确
   - 确认用户有发布文章的权限

### 版本兼容性说明

此项目使用 **OpenAI Python 库 0.27.4 版本**，这是经过测试的稳定版本。新版本的 OpenAI 库可能存在兼容性问题，特别是异常处理部分的 API 发生了变化。

如果遇到 `module 'openai' has no attribute 'error'` 错误，请降级到 0.27.4 版本：

```bash
pip install openai==0.27.4
```

## 🤝 贡献指南

欢迎为这个项目做出贡献！您可以通过以下方式参与：

1. 报告 bug 或提出新功能建议
2. 提交 Pull Request 改进代码
3. 添加新的提示词模板
4. 改进文档

## 📄 许可证

本项目采用 GNU 许可证。详见 [LICENSE](LICENSE) 文件。

## 📋 更新日志

### v1.2.0 (2025-09-01)
- 添加 OpenAI baseURL 配置支持
- 修复 OpenAI 库版本兼容性问题
- 优化配置管理和错误处理

### v1.1.0 (2025-09-01)
- 新增 AI 排版优化模块
- 添加可配置的 OpenAI 参数
- 实现自定义提示词模板系统

### v1.0.0 (2025-08-31)
- 初始版本发布
- 支持手动输入 HTML 内容
- 支持设置文章状态、分类、标签和摘要
- 添加发布前确认机制

---

如有问题或建议，请通过 Issue 反馈或联系开发者。