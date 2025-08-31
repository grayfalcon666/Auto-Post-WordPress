# WordPress HTML 文章发布工具

这是一个通过 WordPress REST API 自动发布 HTML 文章的 Python 工具，允许用户手动输入 HTML 内容并将其发布到 WordPress 网站。

## 功能特性

- ✨ 通过 WordPress REST API 发布文章
- 🎨 支持手动输入 HTML 格式内容
- 📝 灵活的输入方式，使用 `:END` 标记结束输入
- 🔧 可设置文章状态（发布/草稿）
- 🏷️ 支持分类和标签设置
- 📋 提供文章摘要功能
- ✅ 发布前确认机制，避免误操作

## 环境要求

- Python 3.6+
- WordPress 5.6+ (支持应用程序密码功能)
- 已安装 Application Passwords 插件 (如果 WordPress 版本低于 5.6)

## 安装步骤

1. 克隆或下载此项目到本地
2. 安装必要的 Python 依赖：
   ```bash
   pip install requests
   ```
3. 在 WordPress 后台生成应用程序密码：
   - 进入「用户」→「个人资料」
   - 在「应用程序密码」部分创建新密码
   - 复制并保存生成的密码

## 使用方法

1. 编辑 `main()` 函数中的配置信息：
   ```python
   SITE_URL = "https://yourwordpresssite.com"  # 你的WordPress站点地址
   USERNAME = "your_username"                 # 你的WordPress用户名
   APP_PASSWORD = "your_app_password"         # 你的应用程序密码
   ```

2. 运行程序：
   ```bash
   python wordpress_publisher.py
   ```

3. 按照提示输入：
   - 文章标题
   - HTML 内容（输入完成后单独一行输入 `:END`）
   - 发布状态（发布/草稿）
   - 分类ID（可选，多个用逗号分隔）
   - 标签ID（可选，多个用逗号分隔）
   - 文章摘要（可选）

4. 确认发布信息后，文章将被发送到 WordPress

## 输入示例

```
请输入文章标题: 我的测试HTML文章

请输入HTML内容（输入 ':END' 单独一行结束输入）:
<h1>这是一个测试文章</h1>
<p>这是通过<strong>Python程序</strong>发布的HTML内容。</p>
<ul>
    <li>列表项1</li>
    <li>列表项2</li>
</ul>
:END

发布状态 (1: 发布, 2: 草稿) [默认: 1]: 1
分类ID (多个用逗号分隔，直接回车跳过): 1
标签ID (多个用逗号分隔，直接回车跳过): 5,10
文章摘要 (直接回车跳过): 这是一篇测试HTML发布的文章
```

## 故障排除

### 常见问题

1. **认证失败** (401错误)
   - 检查用户名和应用程序密码是否正确
   - 确认 WordPress 站点已启用 REST API

2. **权限不足** (403错误)
   - 确认用户有发布文章的权限（管理员或编辑角色）

3. **连接超时**
   - 检查网络连接
   - 确认 WordPress 站点地址正确

4. **HTML 显示异常**
   - 检查 HTML 代码是否正确
   - WordPress 可能会过滤某些 HTML 标签

### 获取分类和标签 ID

要获取分类和标签的 ID，请登录 WordPress 后台：
- 进入「文章」→「分类」或「文章」→「标签」
- 将鼠标悬停在分类/标签上，浏览器状态栏会显示 ID
- 或者编辑分类/标签，URL 中的 `tag_ID=数字` 就是 ID

## 自定义配置

### 修改结束标记

要更改 HTML 输入的结束标记，编辑 `get_html_content_from_input()` 函数中的这一行：

```python
if line.strip() == ":END":  # 将 ":END" 改为你喜欢的任何标记
```

### 调整超时时间

要修改 API 请求的超时时间，编辑 `create_html_post()` 方法中的 `timeout` 参数：

```python
timeout=30  # 将 30 改为你想要的秒数
```

## 贡献

欢迎提交 Issue 和 Pull Request 来改进这个项目。

## 许可证

本项目采用 MIT 许可证。详见 [LICENSE](LICENSE) 文件。

## 更新日志

### v1.0.0 (2024-01-01)
- 初始版本发布
- 支持手动输入 HTML 内容
- 支持设置文章状态、分类、标签和摘要
- 添加发布前确认机制

---

如有问题，请通过 Issue 反馈或联系开发者。