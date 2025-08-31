import requests
import base64
import json
import os
from ai_formatter import optimize_content, PROMPT_TEMPLATES


class WordPressPublisher:
    def __init__(self, site_url, username, app_password):
        """
        初始化WordPress发布器

        参数:
            site_url: WordPress站点地址 (例如: https://yourwordpresssite.com)
            username: WordPress用户名
            app_password: 应用程序密码(在WordPress用户配置中生成)
        """
        self.site_url = site_url.rstrip('/')
        self.api_url = f"{self.site_url}/wp-json/wp/v2/posts"  # WordPress标准文章API端点
        self.username = username
        self.app_password = app_password

        # 准备Basic Auth认证头
        credentials = f"{username}:{app_password}"
        token = base64.b64encode(credentials.encode()).decode('utf-8')

        self.headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Basic {token}',
            'User-Agent': 'WordPress-HTML-Publisher/1.0'
        }

    def create_html_post(self, title, html_content, status='publish', categories=None, tags=None, excerpt=''):
        """
        发布HTML内容到WordPress

        参数:
            title: 文章标题
            html_content: HTML格式的文章内容
            status: 文章状态 ('draft'草稿, 'publish'立即发布, 'pending'审核)
            categories: 分类ID列表 (可选)
            tags: 标签ID列表 (可选)
            excerpt: 文章摘要 (可选)

        返回:
            成功时返回API响应，失败时返回None
        """
        post_data = {
            'title': title,
            'content': html_content,  # 直接使用HTML内容
            'status': status,
            'excerpt': excerpt,
        }

        # 添加可选分类和标签
        if categories:
            post_data['categories'] = categories
        if tags:
            post_data['tags'] = tags

        try:
            response = requests.post(
                self.api_url,
                headers=self.headers,
                data=json.dumps(post_data),
                timeout=30
            )

            if response.status_code == 201:
                print("HTML文章发布成功！")
                return response.json()
            else:
                print(f"发布失败，状态码: {response.status_code}")
                print(f"错误信息: {response.text}")
                return None

        except requests.exceptions.RequestException as e:
            print(f"请求过程中出现错误: {str(e)}")
            return None


def get_html_content_from_input():
    """
    从用户输入获取HTML内容
    用户可以输入多行HTML，以特殊标记:END结束输入
    """
    print("\n请输入HTML内容（输入 ':END' 单独一行结束输入）:")
    print("提示：可以输入多行HTML代码，完成后输入 ':END' 结束")
    print("=" * 50)

    lines = []
    while True:
        try:
            line = input()
            if line.strip() == ":END":
                break
            lines.append(line)
        except EOFError:
            break

    return "\n".join(lines)


def configure_ai_optimization():
    """
    配置AI优化选项
    """
    print("\n" + "=" * 50)
    print("AI 排版优化配置")
    print("=" * 50)

    # 检查是否已设置API密钥
    if not os.environ.get("OPENAI_API_KEY"):
        api_key = input("请输入OpenAI API密钥: ").strip()
        if api_key:
            os.environ["OPENAI_API_KEY"] = api_key
        else:
            print("未提供API密钥，跳过AI优化")
            return None

    # 选择是否使用AI优化
    use_ai = input("是否使用AI排版优化? (y/N): ").strip().lower()
    if use_ai != 'y':
        return None

    # 选择提示词模板
    print("\n可用的提示词模板:")
    for i, (key, template) in enumerate(PROMPT_TEMPLATES.items(), 1):
        print(f"{i}. {key}: {template[:50]}...")

    print(f"{len(PROMPT_TEMPLATES) + 1}. 自定义提示词")

    template_choice = input(f"请选择提示词模板 (1-{len(PROMPT_TEMPLATES) + 1}) [默认: 1]: ").strip()

    if template_choice == str(len(PROMPT_TEMPLATES) + 1):
        custom_prompt = input("请输入自定义提示词模板 (使用{}作为内容占位符): ").strip()
        prompt_template = custom_prompt
    else:
        try:
            choice_idx = int(template_choice) - 1 if template_choice else 0
            prompt_key = list(PROMPT_TEMPLATES.keys())[choice_idx]
            prompt_template = PROMPT_TEMPLATES[prompt_key]
        except (ValueError, IndexError):
            prompt_key = list(PROMPT_TEMPLATES.keys())[0]
            prompt_template = PROMPT_TEMPLATES[prompt_key]
            print(f"使用默认模板: {prompt_key}")

    # 配置温度参数
    temperature_input = input("温度参数 (0.0-1.0, 控制创造性) [默认: 0.7]: ").strip()
    try:
        temperature = float(temperature_input) if temperature_input else 0.7
    except ValueError:
        temperature = 0.7
        print("使用默认温度: 0.7")

    # 配置最大token数
    max_tokens_input = input("最大token数 (控制响应长度) [默认: 1000]: ").strip()
    try:
        max_tokens = int(max_tokens_input) if max_tokens_input else 1000
    except ValueError:
        max_tokens = 1000
        print("使用默认最大token数: 1000")

    return {
        "prompt_template": prompt_template,
        "temperature": temperature,
        "max_tokens": max_tokens
    }


def main():
    # 配置你的WordPress信息
    SITE_URL = "https://blog.jamaisvu.tech"  # 你的WordPress站点地址
    USERNAME = "your_username"  # 替换为你的WordPress用户名
    APP_PASSWORD = "your_app_password"  # 替换为你的应用程序密码

    # 初始化发布器
    publisher = WordPressPublisher(SITE_URL, USERNAME, APP_PASSWORD)

    # 获取文章标题
    title = input("请输入文章标题: ").strip()
    if not title:
        print("标题不能为空，程序退出")
        return

    # 获取HTML内容
    html_content = get_html_content_from_input()
    if not html_content.strip():
        print("HTML内容不能为空，程序退出")
        return

    # 配置AI优化选项
    ai_config = configure_ai_optimization()

    # 如果配置了AI优化，则应用优化
    if ai_config:
        print("\n正在使用AI优化内容...")
        try:
            optimized_content = optimize_content(
                html_content,
                prompt_template=ai_config["prompt_template"],
                temperature=ai_config["temperature"],
                max_tokens=ai_config["max_tokens"]
            )

            print("\n优化前内容预览:")
            print(html_content[:200] + "..." if len(html_content) > 200 else html_content)
            print("\n优化后内容预览:")
            print(optimized_content[:200] + "..." if len(optimized_content) > 200 else optimized_content)

            use_optimized = input("\n是否使用优化后的内容? (Y/n): ").strip().lower()
            if use_optimized != 'n':
                html_content = optimized_content
                print("已使用优化后的内容")
            else:
                print("保留原始内容")

        except Exception as e:
            print(f"AI优化过程中出错: {str(e)}")
            print("将继续使用原始内容")

    # 确认发布状态
    status_choice = input("\n发布状态 (1: 发布, 2: 草稿) [默认: 1]: ").strip()
    status = 'publish' if status_choice != '2' else 'draft'

    # 可选：获取分类和标签
    categories_input = input("分类ID (多个用逗号分隔，直接回车跳过): ").strip()
    categories = [int(cid.strip()) for cid in categories_input.split(',')] if categories_input else None

    tags_input = input("标签ID (多个用逗号分隔，直接回车跳过): ").strip()
    tags = [int(tid.strip()) for tid in tags_input.split(',')] if tags_input else None

    # 可选：获取摘要
    excerpt = input("文章摘要 (直接回车跳过): ").strip()

    # 确认发布
    print("\n" + "=" * 50)
    print("即将发布文章:")
    print(f"标题: {title}")
    print(f"状态: {'发布' if status == 'publish' else '草稿'}")
    print(f"内容长度: {len(html_content)} 字符")
    print("内容预览:")
    print(html_content[:200] + "..." if len(html_content) > 200 else html_content)
    print("=" * 50)

    confirm = input("确认发布? (y/N): ").strip().lower()
    if confirm != 'y':
        print("取消发布")
        return

    # 发布文章
    result = publisher.create_html_post(
        title=title,
        html_content=html_content,
        status=status,
        categories=categories,
        tags=tags,
        excerpt=excerpt if excerpt else ''
    )

    if result:
        print(f"✅ 文章创建成功！")
        print(f"   文章ID: {result.get('id', 'N/A')}")
        print(f"   文章标题: {result.get('title', {}).get('rendered', 'N/A')}")
        print(f"   文章链接: {result.get('link', 'N/A')}")
        print(f"   编辑链接: {result.get('link', '').replace('?p=', '/wp-admin/post.php?post=')}&action=edit")
    else:
        print("❌ 文章发布失败")


if __name__ == "__main__":
    main()