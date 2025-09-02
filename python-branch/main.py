import requests
import base64
import json
from config import WORDPRESS, OPENAI, PROMPT_TEMPLATES, APP


class WordPressPublisher:
    def __init__(self):
        """
        初始化WordPress发布器，使用config.py中的配置
        """
        self.site_url = WORDPRESS["SITE_URL"].rstrip('/')
        self.api_url = f"{self.site_url}/wp-json/wp/v2/posts"
        self.username = WORDPRESS["USERNAME"]
        self.app_password = WORDPRESS["APP_PASSWORD"]

        # 准备Basic Auth认证头
        credentials = f"{self.username}:{self.app_password}"
        token = base64.b64encode(credentials.encode()).decode('utf-8')

        self.headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Basic {token}',
            'User-Agent': 'WordPress-HTML-Publisher/1.0'
        }

    def create_html_post(self, title, html_content, status=None, categories=None, tags=None, excerpt=''):
        """
        发布HTML内容到WordPress
        """
        # 使用配置中的默认状态或传入的状态
        post_status = status if status else APP["DEFAULT_STATUS"]

        post_data = {
            'title': title,
            'content': html_content,
            'status': post_status,
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
                timeout=APP["TIMEOUT"]
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


def ask_ai_optimization():
    """
    询问是否使用AI优化
    """
    print("\n" + "=" * 50)
    print("AI 排版优化选项")
    print("=" * 50)

    # 使用配置中的默认设置
    default_choice = "y" if APP["ENABLE_AI_BY_DEFAULT"] else "n"
    prompt = f"是否使用AI排版优化? (Y/n) [默认: {'是' if default_choice == 'y' else '否'}]: "

    use_ai = input(prompt).strip().lower()
    if not use_ai:  # 如果用户直接回车，使用默认值
        use_ai = default_choice

    return use_ai == 'y'


def configure_ai_optimization():
    """
    配置AI优化选项
    """
    # 检查是否已设置API密钥
    if not OPENAI["API_KEY"] or OPENAI["API_KEY"] == "your_openai_api_key":
        api_key = input("请输入OpenAI API密钥 (直接回车跳过AI优化): ").strip()
        if api_key:
            # 更新配置（仅本次运行有效）
            OPENAI["API_KEY"] = api_key
        else:
            print("未提供API密钥，跳过AI优化")
            return None

    # 选择提示词模板
    print("\n可用的提示词模板:")
    templates = {
        "1": "default: 标准优化",
        "2": "technical: 技术文档优化",
        "3": "creative: 创意写作优化",
        "4": "seo: SEO优化",
        "5": "minimal: 简洁优化"
    }

    for key, desc in templates.items():
        print(f"{key}. {desc}")

    template_choice = input("请选择提示词模板 (1-5) [默认: 1]: ").strip() or "1"

    # 配置温度参数
    temperature_input = input(f"温度参数 (0.0-1.0, 控制创造性) [默认: {OPENAI['DEFAULT_TEMPERATURE']}]: ").strip()
    try:
        temperature = float(temperature_input) if temperature_input else OPENAI["DEFAULT_TEMPERATURE"]
    except ValueError:
        temperature = OPENAI["DEFAULT_TEMPERATURE"]
        print(f"使用默认温度: {temperature}")

    # 配置最大token数
    max_tokens_input = input(f"最大token数 (控制响应长度) [默认: {OPENAI['DEFAULT_MAX_TOKENS']}]: ").strip()
    try:
        max_tokens = int(max_tokens_input) if max_tokens_input else OPENAI["DEFAULT_MAX_TOKENS"]
    except ValueError:
        max_tokens = OPENAI["DEFAULT_MAX_TOKENS"]
        print(f"使用默认最大token数: {max_tokens}")

    return {
        "template_choice": template_choice,
        "temperature": temperature,
        "max_tokens": max_tokens
    }


def optimize_content_with_ai(content, ai_config):
    """
    使用AI优化内容
    """
    try:
        # 动态导入AI模块
        from ai_formatter import optimize_content

        # 选择模板
        templates_map = {
            "1": "default",
            "2": "technical",
            "3": "creative",
            "4": "seo",
            "5": "minimal"
        }

        template_key = templates_map.get(ai_config["template_choice"], "default")
        prompt_template = PROMPT_TEMPLATES.get(template_key, PROMPT_TEMPLATES["default"])

        print("\n正在使用AI优化内容...")
        optimized_content = optimize_content(
            content,
            prompt_template=prompt_template,
            temperature=ai_config["temperature"],
            max_tokens=ai_config["max_tokens"]
        )

        print("\n优化前内容预览:")
        print(content[:200] + "..." if len(content) > 200 else content)
        print("\n优化后内容预览:")
        print(optimized_content[:200] + "..." if len(optimized_content) > 200 else optimized_content)

        use_optimized = input("\n是否使用优化后的内容? (Y/n): ").strip().lower()
        if use_optimized != 'n':
            return optimized_content
        else:
            print("保留原始内容")
            return content

    except ImportError:
        print("AI模块导入失败，跳过优化")
        return content
    except Exception as e:
        print(f"AI优化过程中出错: {str(e)}")
        print("将继续使用原始内容")
        return content


def main():
    # 初始化发布器
    publisher = WordPressPublisher()

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

    # 询问是否使用AI优化
    use_ai = ask_ai_optimization()

    # 如果选择使用AI优化，则配置并应用优化
    if use_ai:
        ai_config = configure_ai_optimization()
        if ai_config:  # 只有在成功配置AI时才进行优化
            html_content = optimize_content_with_ai(html_content, ai_config)

    # 确认发布状态
    status_choice = input(f"\n发布状态 (1: 发布, 2: 草稿) [默认: {APP['DEFAULT_STATUS']}]: ").strip()
    if status_choice == "2":
        status = 'draft'
    else:
        status = APP["DEFAULT_STATUS"]

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