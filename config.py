# -*- coding: utf-8 -*-
"""
WordPress 文章发布工具配置文件
请根据您的实际情况修改以下配置
"""

# ==================== WordPress 配置 ====================
WORDPRESS = {
    "SITE_URL": "https://blog.jamaisvu.tech",  # 你的WordPress站点地址
    "USERNAME": "your_username",               # 你的WordPress用户名
    "APP_PASSWORD": "your_app_password",       # 你的应用程序密码
}

# ==================== OpenAI 配置 ====================
OPENAI = {
    "API_KEY": "your_openai_api_key",          # 你的OpenAI API密钥
    "BASE_URL": "https://api.openai.com/v1",   # OpenAI API基础URL (对于Azure OpenAI或其他兼容API，请修改此项)
    "DEFAULT_MODEL": "gpt-3.5-turbo",          # 默认模型
    "DEFAULT_TEMPERATURE": 0.7,                # 默认温度参数 (0.0-1.0)
    "DEFAULT_MAX_TOKENS": 1000,                # 默认最大token数
}

# ==================== AI 提示词模板配置 ====================
PROMPT_TEMPLATES = {
    "default": "请优化以下内容的排版，使其更易读和专业：\n\n{}",
    "technical": "作为技术文档专家，请优化以下技术内容的排版，确保专业性和准确性：\n\n{}",
    "creative": "请以创意写作的方式优化以下内容，使其更生动有趣，同时保持原意：\n\n{}",
    "seo": "请优化以下内容的排版，使其更适合搜索引擎优化，同时保持可读性：\n\n{}",
    "minimal": "请简洁地优化以下内容的排版，去除冗余，保持核心信息：\n\n{}"
}

# ==================== 应用程序配置 ====================
APP = {
    "DEFAULT_STATUS": "publish",               # 默认发布状态 (publish/draft)
    "ENABLE_AI_BY_DEFAULT": False,             # 是否默认启用AI优化
    "TIMEOUT": 30,                             # 请求超时时间(秒)
}