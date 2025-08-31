# WordPress Article Publishing Tool with AI Formatting Optimization  

A Python tool that automates article publishing to WordPress via the WordPress REST API and integrates AI-powered content formatting optimization. It supports HTML content input and AI-assisted content refinement.  


## ✨ Key Features  
- **WordPress Article Publishing**: Automatically publish articles to WordPress using the REST API.  
- **HTML Content Support**: Enable manual input of HTML-formatted content.  
- **AI Formatting Optimization**: Integrate OpenAI GPT models to optimize content structure and readability.  
- **Centralized Configuration**: Manage all settings in a single config file, with support for custom prompt templates.  
- **Interactive Interface**: User-friendly command-line interface (CLI) for seamless operation.  
- **Error Handling**: Comprehensive error handling and clear user prompts for troubleshooting.  


## 📁 Project Structure  
```
wordpress-ai-publisher/
├── main.py                 # Main Program - WordPress Article Publishing Tool
├── ai_formatter.py         # AI Formatting Optimization Module
├── config.py               # Centralized Configuration File
├── requirements.txt        # Project Dependencies
└── README.md               # Project Documentation
```  


## 🛠️ Installation & Configuration  

### Prerequisites  
- Python 3.6 or higher  
- WordPress 5.6 or higher (supports the **Application Password** feature)  
- An OpenAI API account  


### Installation Steps  
1. Clone or download the project to your local machine.  
2. Install required Python dependencies:  
   ```bash
   pip install -r requirements.txt
   ```  
3. Configure the `config.py` file:  
   - Set your WordPress site URL, username, and application password.  
   - Configure your OpenAI API key and other parameters.  
4. Generate a WordPress Application Password in the WordPress admin panel:  
   - Navigate to **Users** → **Profile**.  
   - Create a new password under the **Application Passwords** section.  
   - Copy and save the generated password for later use.  


## ⚙️ Configuration Details  

Edit the `config.py` file to customize settings for your workflow:  

### WordPress Configuration  
```python
WORDPRESS = {
    "SITE_URL": "https://yourwordpresssite.com",  # Your WordPress site URL
    "USERNAME": "your_username",                  # Your WordPress username
    "APP_PASSWORD": "your_app_password",          # Your WordPress Application Password
}
```  

### OpenAI Configuration  
```python
OPENAI = {
    "API_KEY": "your_openai_api_key",             # Your OpenAI API key
    "BASE_URL": "https://api.openai.com/v1",      # OpenAI API base URL
    "DEFAULT_MODEL": "gpt-3.5-turbo",             # Default AI model
    "DEFAULT_TEMPERATURE": 0.7,                   # Default temperature (0.0-1.0)
    "DEFAULT_MAX_TOKENS": 1000,                   # Default maximum tokens for AI responses
}
```  

### Prompt Template Configuration  
```python
PROMPT_TEMPLATES = {
    "default": "Optimize the formatting of the following content to improve readability and professionalism:\n\n{}",
    "technical": "As a technical documentation expert, optimize the formatting of the following technical content:\n\n{}",
    "creative": "Optimize the following content with a creative writing style to make it more engaging:\n\n{}",
    # Add your custom templates here...
}
```  


## 🚀 Usage Guide  

### Basic Usage  
1. Run the main program:  
   ```bash
   python main.py
   ```  
2. Follow the CLI prompts to input:  
   - Article title  
   - HTML content (enter `:END` to finish inputting content)  
   - Whether to use AI formatting optimization  
   - Publication status (Published/Draft)  
   - Category and tag IDs (optional)  
   - Article excerpt (optional)  
3. After confirming the publication details, the article will be sent to your WordPress site.  


### AI Formatting Optimization  
When you select AI formatting optimization, the program will prompt you to configure:  
1. **Prompt Template**: Choose a predefined template or use a custom prompt to guide AI optimization.  
2. **Temperature**: Adjust AI creativity (range: 0.0–1.0; default: 0.7).  
3. **Max Tokens**: Limit the length of the AI’s response.  


## 🔧 Advanced Usage  

### Using the AI Formatting Module Independently  
You can use the `ai_formatter.py` module separately to optimize any text content:  
```python
from ai_formatter import optimize_content

# Optimize content
original_content = "Your original content here..."
optimized_content = optimize_content(
    original_content,
    prompt_template="default",
    temperature=0.7,
    max_tokens=1000
)

print(f"Before Optimization: {original_content}")
print(f"After Optimization: {optimized_content}")
```  

### Customizing Prompt Templates  
Add or modify prompt templates in the `PROMPT_TEMPLATES` dictionary within `config.py`:  
```python
PROMPT_TEMPLATES = {
    "default": "Optimize the formatting of the following content to improve readability and professionalism:\n\n{}",
    "technical": "As a technical documentation expert, optimize the formatting of the following technical content:\n\n{}",
    "creative": "Optimize the following content with a creative writing style to make it more engaging:\n\n{}",
    "academic": "Refine the following academic content to meet formal writing standards and improve clarity:\n\n{}",  # Custom template
    # Add more templates here...
}
```  


## 🐛 Troubleshooting  

### Common Issues  
1. **OpenAI API Errors**  
   - Ensure your OpenAI API key is correctly configured in `config.py`.  
   - Verify your API key has sufficient credits.  
   - **Note**: This project uses **OpenAI Python Library v0.27.4** (a tested stable version). Newer versions may have compatibility issues.  

2. **WordPress Connection Issues**  
   - Double-check your WordPress site URL, username, and application password in `config.py`.  
   - Confirm the WordPress REST API is enabled (enabled by default in WordPress 5.6+).  
   - Ensure your WordPress user has permission to publish articles.  

3. **401 Unauthorized Error**  
   - Verify your WordPress application password is correct.  
   - Confirm your user account has the "Publish Posts" capability in WordPress.  


### Version Compatibility Note  
This project is tested with **OpenAI Python Library v0.27.4**. Newer versions may break compatibility (especially changes to error handling APIs).  

If you encounter the error `module 'openai' has no attribute 'error'`, downgrade to v0.27.4:  
```bash
pip install openai==0.27.4
```  


## 🤝 Contribution Guidelines  
Contributions to this project are welcome! You can participate by:  
1. Reporting bugs or suggesting new features via Issues.  
2. Submitting Pull Requests to improve code quality or add functionality.  
3. Adding custom prompt templates for different content types.  
4. Enhancing project documentation.  


## 📄 License  
This project is licensed under the **GNU General Public License (GPL)**. See the [LICENSE](LICENSE) file for details.  


## 📋 Changelog  

### v1.2.0 (2025-09-01)  
- Added support for configuring the OpenAI API base URL.  
- Fixed compatibility issues with the OpenAI Python library.  
- Improved configuration management and error handling.  

### v1.1.0 (2025-09-01)  
- Added the AI Formatting Optimization Module.  
- Implemented configurable OpenAI parameters.  
- Added support for custom prompt templates.  

### v1.0.0 (2025-08-31)  
- Initial release.  
- Supported manual input of HTML content.  
- Enabled setting article status, categories, tags, and excerpts.  
- Added pre-publication confirmation to prevent accidental submissions.  


---  
For questions or suggestions, please provide feedback via Issues or contact the developer.