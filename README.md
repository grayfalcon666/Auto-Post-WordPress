# 跨平台 WordPress 文章发布工具（Python + Flutter）

一个支持 **PC端（Python）** 和 **安卓端（Flutter）** 的 WordPress 文章自动发布工具，Python 端集成 AI 排版优化功能，Flutter 端支持安卓设备开箱即用，均通过 WordPress REST API 实现核心发布能力，兼顾灵活性与便携性。


## ✨ 功能特点

### 🔹 Python 端（PC）
- **WordPress 文章发布**：通过 REST API 自动发布文章到 WordPress
- **HTML 与 MARKDOWN 内容支持**：支持手动输入 HTML 及 MD 格式内容
- **AI 排版优化**：集成 OpenAI GPT 模型进行内容优化和排版
- **灵活配置**：所有配置集中管理（`config.py`），支持自定义提示词模板
- **交互式界面**：用户友好的命令行交互界面，步骤清晰
- **完善错误处理**：详细的错误提示与异常捕获，便于排查问题

### 🔹 Flutter 端（安卓）
- **安卓开箱即用**：直接安装 APK 即可使用，无需额外环境配置
- **简洁可视化 UI**：针对安卓设备优化的界面，分为「配置页」和「发布页」
- **本地配置存储**：通过 `SharedPreferences` 持久化保存 WordPress 配置，无需重复输入
- **核心发布功能**：支持输入文章标题、HTML 内容、选择发布状态（草稿/发布）
- **可选字段支持**：可配置文章分类 ID、标签 ID、摘要
- **发布结果反馈**：发布成功/失败提示，支持直接查看文章链接


## 📁 项目结构

```
Auto-Post-WordPress/
├─.idea
│  └─inspectionProfiles
├─flutter-branch
│  └─lib
│      ├─models
│      ├─services
│      └─widgets
├─python-branch
└─__pycache__
```


## 🛠️ 安装与配置

### 🔹 Python 端（PC）安装与配置

#### 环境要求
- Python 3.6+
- WordPress 5.6+（需支持「应用程序密码」功能）
- OpenAI API 账户（使用 AI 优化时需配置）

#### 安装步骤
1. 进入 `python-branch` 目录：
   ```bash
   cd python-branch
   ```
2. 安装依赖：
   ```bash
   pip install -r ../requirements.txt
   ```
3. 配置 `config.py` 文件：
   - **WordPress 配置**：设置站点 URL、用户名、应用程序密码
   - **OpenAI 配置**（可选）：填入 API 密钥、选择默认模型（如 `gpt-3.5-turbo`）
   - **提示词模板**（可选）：自定义 AI 优化的提示词模板
4. 生成 WordPress 应用程序密码：
   - 登录 WordPress 后台 → 「用户」→「个人资料」
   - 拉到「应用程序密码」区域 → 输入应用名称（如「Python 发布工具」）→ 点击「生成」
   - 复制生成的 16 位密码（格式：xxxx xxxx xxxx xxxx），填入 `config.py` 的 `APP_PASSWORD`


### 🔹 Flutter 端（安卓）安装与配置

#### 环境要求
- Flutter 3.0+（开发环境，如需二次开发）
- 安卓设备/模拟器（Android 5.0+，API 级别 21+）
- 已生成的 Flutter 端 APK 文件（开箱即用，无需开发环境）

#### 安装步骤（开箱即用）
1. 获取 Flutter 端 APK 文件：
   - 从项目编译产物中获取 `app-release.apk`（路径：`flutter-branch/build/app/outputs/apk/release/`）
2. 安装到安卓设备：
   - 将 APK 传输到安卓设备 → 点击安装（需开启「未知来源应用安装」权限）
3. 安卓端配置（首次打开 APP）：
   - 进入「WordPress 配置」页面 → 输入：
     - 站点 URL（如 `https://your-wordpress-site.com`，需带 `https://`）
     - WordPress 用户名
     - WordPress 应用程序密码（同 Python 端生成的密码）
   - 点击「保存配置」→ 验证通过后自动跳转至「发布页面」

#### 开发环境配置（二次开发）
1. 进入 `flutter-branch` 目录：
   ```bash
   cd flutter-branch
   ```
2. 安装 Flutter 依赖：
   ```bash
   flutter pub get
   ```
3. 安卓端额外配置：
   - 网络权限：确保 `android/app/src/main/AndroidManifest.xml` 中已添加：
     ```xml
     <uses-permission android:name="android.permission.INTERNET" />
     ```
4. 生成 APK：
   ```bash
   flutter build apk --release
   ```


## 🚀 使用方法

### 🔹 Python 端（PC）使用

#### 基本使用
1. 运行主程序：
   ```bash
   cd python-branch
   python main.py
   ```
2. 按照命令行提示输入：
   - 文章标题（必填）
   - HTML 内容（输入完成后单独一行输入 `:END` 结束，必填）
   - 是否使用 AI 排版优化（输入 `y`/`n`，可选）
   - 发布状态（`1` 为发布，`2` 为草稿，默认草稿）
   - 分类 ID/标签 ID（多个用逗号分隔，可选）
   - 文章摘要（可选）
3. 确认发布信息 → 程序自动发送请求到 WordPress，返回发布结果（成功/失败）

#### AI 排版优化（Python 端特有）
当选择「使用 AI 优化」时，需配置：
1. 提示词模板（选择预设模板：标准优化/技术文档优化/创意写作优化等）
2. 温度参数（0.0-1.0，值越高创造性越强，默认 0.7）
3. 最大 token 数（限制 AI 响应长度，默认 1000）
4. 优化完成后会显示「优化前/后预览」→ 选择是否使用优化后的内容


### 🔹 Flutter 端（安卓）使用

#### 配置 WordPress 信息
1. 打开 APP → 首次使用自动进入「配置页面」：
   - 输入站点 URL（如 `https://blog.example.com`，需完整且正确）
   - 输入 WordPress 用户名和应用程序密码
   - 点击「保存配置」→ 验证通过后跳转至「发布页面」
   - （如需修改配置）点击右上角「设置」图标 → 重新进入配置页面

#### 发布文章
1. 在「发布页面」输入：
   - **文章标题**（必填，不能为空）
   - **文章内容**（HTML 格式，如 `<p>正文内容</p>`，必填）
   - **发布状态**（选择「草稿」或「立即发布」）
   - **分类 ID**（可选，多个用逗号分隔，如 `1,3`）
   - **标签 ID**（可选，格式同上）
   - **文章摘要**（可选）
2. 点击底部「发布」按钮（根据状态显示「保存为草稿」或「立即发布」）：
   - 发布成功：弹出提示，显示文章 ID 和查看链接，支持点击「查看文章」跳转至浏览器
   - 发布失败：弹出错误原因（如配置错误、网络问题）


## 🔧 高级用法

### 🔹 Python 端高级用法
#### 单独使用 AI 排版优化模块
可在其他 Python 项目中引入 `ai_formatter.py` 优化文本：
```python
from ai_formatter import optimize_content

# 原始内容
original_content = "这是一篇技术文章，需要优化排版和可读性..."
# 优化内容
optimized_content = optimize_content(
    original_content,
    prompt_template="technical",  # 使用技术文档优化模板
    temperature=0.6,              # 降低创造性，更严谨
    max_tokens=1500               # 增加最大响应长度
)

print("优化前：", original_content)
print("优化后：", optimized_content)
```

#### 自定义提示词模板
编辑 `python-branch/config.py` 中的 `PROMPT_TEMPLATES` 字典：
```python
PROMPT_TEMPLATES = {
    "default": "请优化以下内容的排版，使其更易读和专业：\n\n{}",
    "technical": "作为技术文档专家，请优化以下技术内容的排版：\n\n{}",
    "seo": "作为SEO优化专家，请优化内容排版并提升关键词密度：\n\n{}",  # 新增SEO模板
    "short": "请将内容优化为简洁短文本，适合移动端阅读：\n\n{}"       # 新增短文本模板
}
```


### 🔹 Flutter 端高级用法
#### 查看/编辑配置
- 点击「发布页面」右上角「设置」图标 → 进入配置页面，可修改 WordPress 信息
- 配置变更后会自动验证有效性，确保后续发布正常

#### APK 签名配置（正式发布）
如需将 APK 上架应用商店，需配置自定义签名：
1. 生成签名文件（参考前文 `keytool` 命令）
2. 在 `flutter-branch/android` 目录下创建 `key.properties`：
   ```properties
   keyAlias=mykey
   keyPassword=你的密钥密码
   storeFile=D:/path/to/your/key.jks
   storePassword=你的密钥库密码
   ```
3. 修改 `flutter-branch/android/app/build.gradle.kts` 中的签名配置（参考前文修正后的代码）


## 🐛 故障排除

### 🔹 Python 端常见问题
1. **OpenAI API 错误**
   - 检查 `config.py` 中 API 密钥是否正确，且有足够余额
   - 若提示「module 'openai' has no attribute 'error'」，降级 OpenAI 库：
     ```bash
     pip install openai==0.27.4
     ```

2. **WordPress 401 未授权错误**
   - 确认用户名和应用程序密码是否匹配（应用程序密码不是登录密码）
   - 检查 WordPress 用户是否有「发布文章」权限

3. **WordPress API 连接失败**
   - 确认站点 URL 正确（需带 `https://`，且无多余斜杠）
   - 检查 WordPress REST API 是否正常（访问 `https://your-site.com/wp-json/wp/v2/posts` 应返回 JSON 数据）


### 🔹 Flutter 端常见问题
1. **配置验证失败**
   - 检查站点 URL 是否完整（必须带 `https://`，如 `https://blog.example.com`）
   - 确认应用程序密码是否正确（避免空格或拼写错误）
   - 检查安卓设备网络是否正常（需能访问 WordPress 站点）

2. **APK 安装失败**
   - 确保安卓设备系统版本 ≥ Android 5.0（API 21+）
   - 关闭「应用安装拦截」功能，或在「设置-安全」中允许未知来源安装

3. **发布时提示「网络错误」**
   - 检查设备网络（Wi-Fi/流量）是否正常
   - 若 WordPress 站点为 HTTP 协议，需在 `AndroidManifest.xml` 中添加：
     ```xml
     <application android:usesCleartextTraffic="true" ...>
     ```


## 🤝 贡献指南

欢迎为这个跨平台项目做出贡献！您可以通过以下方式参与：
1. 报告 bug 或提出新功能建议（Python 端/Flutter 端均可）
2. 提交 Pull Request 改进代码（如优化 UI、修复漏洞、新增功能）
3. 扩展提示词模板（Python 端 AI 优化）
4. 完善文档（补充使用案例、故障排除方案）


## 📄 许可证

本项目采用 **GNU 许可证**。详见 [LICENSE](LICENSE) 文件。


## 📋 更新日志

### v2.0.0 (2025-09-02)
- 新增 Flutter 安卓端，支持安卓设备开箱即用
- 实现 Flutter 端核心功能：WordPress 配置存储、文章发布（草稿/发布）、发布结果反馈
- 优化项目结构，拆分 `python-branch`（原 PC 端）和 `flutter-branch`（新增安卓端）
- 统一 WordPress 认证逻辑，Python 端与 Flutter 端共享应用程序密码配置

### v1.2.0 (2025-09-01)
- 添加 OpenAI baseURL 配置支持
- 修复 OpenAI 库版本兼容性问题
- 优化配置管理和错误处理

### v1.1.0 (2025-09-01)
- 新增 AI 排版优化模块
- 添加可配置的 OpenAI 参数
- 实现自定义提示词模板系统

### v1.0.0 (2025-08-31)
- 初始版本发布（仅 Python 端）
- 支持手动输入 HTML 内容
- 支持设置文章状态、分类、标签和摘要
- 添加发布前确认机制