import openai
import os
from config import OPENAI, PROMPT_TEMPLATES


def optimize_content(content, prompt_template=None, temperature=None, max_tokens=None, model=None):
    """
    使用OpenAI API优化内容排版

    参数:
        content: 需要优化的原始内容
        prompt_template: 提示词模板，使用{}作为内容占位符
        temperature: 控制生成文本的创造性 (0.0-1.0)
        max_tokens: 生成的最大token数量
        model: 使用的OpenAI模型

    返回:
        优化后的内容
    """
    # 检查API密钥
    api_key = OPENAI["API_KEY"]
    if not api_key or api_key == "your_openai_api_key":
        raise ValueError("OpenAI API密钥未设置，请在config.py中配置或运行时输入")

    # 设置OpenAI API密钥和基础URL
    openai.api_key = api_key

    # 如果配置了自定义基础URL，则设置它
    if OPENAI["BASE_URL"] and OPENAI["BASE_URL"] != "https://api.openai.com/v1":
        openai.api_base = OPENAI["BASE_URL"]

    # 使用默认值如果参数未提供
    if prompt_template is None:
        prompt_template = PROMPT_TEMPLATES["default"]

    if temperature is None:
        temperature = OPENAI["DEFAULT_TEMPERATURE"]

    if max_tokens is None:
        max_tokens = OPENAI["DEFAULT_MAX_TOKENS"]

    if model is None:
        model = OPENAI["DEFAULT_MODEL"]

    # 构建完整的提示词
    full_prompt = prompt_template.format(content)

    try:
        # 调用OpenAI API
        response = openai.ChatCompletion.create(
            model=model,
            messages=[
                {"role": "system", "content": "你是一个专业的文本排版优化助手。"},
                {"role": "user", "content": full_prompt}
            ],
            temperature=temperature,
            max_tokens=max_tokens
        )

        # 提取优化后的内容
        optimized_content = response.choices[0].message.content.strip()

        return optimized_content

    except openai.AuthenticationError:
        raise ValueError("OpenAI API密钥无效，请检查config.py中的API密钥配置")

    except openai.RateLimitError:
        raise Exception("API请求速率限制，请稍后再试")

    except openai.APIConnectionError:
        raise Exception("网络连接错误，请检查您的网络连接")

    except openai.APIError as e:
        raise Exception(f"OpenAI API错误: {str(e)}")


def list_available_models():
    """
    列出可用的OpenAI模型
    注意：需要适当的API权限
    """
    try:
        models = openai.Model.list()
        return [model.id for model in models.data]
    except Exception as e:
        print(f"获取模型列表时出错: {str(e)}")
        return []


def test_connection():
    """
    测试OpenAI API连接
    """
    try:
        # 简单的API调用测试
        openai.Model.list()
        return True
    except Exception as e:
        print(f"连接测试失败: {str(e)}")
        return False


if __name__ == "__main__":
    # 模块测试代码
    print("AI Formatter 模块测试")

    # 测试API连接
    if test_connection():
        print("✅ API连接测试成功")

        # 测试内容优化
        test_content = "这是一个测试内容，请优化它的排版。"
        print(f"测试内容: {test_content}")

        try:
            optimized = optimize_content(test_content)
            print(f"优化结果: {optimized}")
        except Exception as e:
            print(f"优化测试失败: {str(e)}")
    else:
        print("❌ API连接测试失败")