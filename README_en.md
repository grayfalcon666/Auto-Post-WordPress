# WordPress Article Publishing Tool with AI Formatting Optimization

This project consists of two core components: a WordPress article publishing tool and an AI formatting optimization module. These components work together to help users create and refine blog content efficiently.


## Project Structure
```
wordpress-ai-publisher/
├── main.py                 # Main Program - WordPress Article Publishing Tool
├── ai_formatter.py         # AI Formatting Optimization Module
├── config.py               # Configuration File (Optional)
├── requirements.txt        # Project Dependencies
└── README.md               # Project Documentation
```


## Feature Highlights

### WordPress Article Publishing Tool (`main.py`)
- ✨ Publish articles via the **WordPress REST API**
- 🎨 Support manual input of HTML-formatted content
- 📝 Flexible input method with `:END` marker to terminate input
- 🔧 Configurable article status (Published/Draft)
- 🏷️ Support for setting categories and tags
- 📋 Article excerpt functionality
- ✅ Pre-publishing confirmation to prevent accidental operations


### AI Formatting Optimization Module (`ai_formatter.py`)
- 🤖 Integrate **OpenAI GPT models** for content optimization
- 🎛️ Configurable AI parameters (temperature, max tokens, etc.)
- 📝 Custom prompt template system
- ⚙️ User-adjustable optimization intensity and quality
- 🔄 Support for multi-round optimization and previews


## Installation & Configuration

### Prerequisites
- Python 3.6+
- WordPress 5.6+ (supports the **Application Password** feature)
- OpenAI API account and API key


### Installation Steps
1. Clone or download the project to your local machine.
2. Install required Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```
   Or install manually:
   ```bash
   pip install requests openai
   ```
3. Configure your OpenAI API key:
   ```bash
   export OPENAI_API_KEY='your-openai-api-key'
   ```
   *Directly setting the key in code is not recommended due to security risks.*

4. Generate a WordPress Application Password in the WordPress admin panel:
   - Navigate to **Users** → **Profile**
   - Create a new password under the **Application Passwords** section
   - Copy and save the generated password for later use


## Usage Guide

### Basic Usage
1. Run the main program:
   ```bash
   python main.py
   ```

2. Follow the prompts to enter article content and other details (e.g., title, categories).

3. When asked whether to use AI formatting optimization, select `y` (yes) or `n` (no).

4. If AI optimization is selected, follow the prompts to configure optimization parameters.

5. After confirming the publishing details, the article will be sent to your WordPress site.


### AI Formatting Optimization Configuration
When AI optimization is enabled, the program provides the following configuration options:
1. **Prompt Template**: Select or customize the prompt used to guide AI optimization.
2. **Temperature Parameter**: Controls AI creativity (range: 0.0–1.0, default: 0.7).
3. **Max Tokens**: Limits the length of the AI's response.
4. **Optimization Intensity**: Adjusts the depth of formatting improvements.


### Customizing Prompt Templates
You can customize prompt templates by editing the `PROMPT_TEMPLATES` dictionary in `ai_formatter.py`:
```python
PROMPT_TEMPLATES = {
    "default": "Please optimize the formatting of the following content to make it more readable and professional:\n\n{}",
    "technical": "As a technical documentation expert, optimize the formatting of the following technical content:\n\n{}",
    "creative": "Optimize the following content with a creative writing style to make it more engaging:\n\n{}",
    # Add your custom templates here...
}
```


## Configuration Options

### OpenAI Parameter Configuration
In `ai_formatter.py`, you can adjust the following default OpenAI parameters:
```python
# Default OpenAI Parameters
DEFAULT_TEMPERATURE = 0.7
DEFAULT_MAX_TOKENS = 1000
DEFAULT_MODEL = "gpt-3.5-turbo"
```


### WordPress Parameter Configuration
In `main.py`, you can set default WordPress configurations:
```python
# Default WordPress Configurations
DEFAULT_SITE_URL = "https://yourwordpresssite.com"
DEFAULT_USERNAME = "your_username"
DEFAULT_APP_PASSWORD = "your_app_password"
```


## Advanced Usage

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


### Batch Processing Articles
Modify the main program to support batch publishing of multiple articles:
```python
# Example: Batch Processing Code
articles = [
    {"title": "Article 1", "content": "Content for Article 1..."},
    {"title": "Article 2", "content": "Content for Article 2..."},
    # Add more articles here...
]

for article in articles:
    # Apply AI optimization (if enabled)
    if use_ai_optimization:
        article["content"] = optimize_content(article["content"])
    
    # Publish to WordPress
    result = publisher.create_html_post(
        title=article["title"],
        html_content=article["content"],
        status=status  # "publish" or "draft"
    )
```


## Troubleshooting

### Common Issues
1. **OpenAI API Errors**
   - Verify that your API key is correctly configured.
   - Ensure your API key has sufficient credits.

2. **WordPress Connection Issues**
   - Double-check the site URL, username, and application password.
   - Confirm the **WordPress REST API** is enabled (default for WordPress 5.6+).

3. **Poor AI Optimization Results**
   - Try adjusting the `temperature` parameter (lower = more precise, higher = more creative).
   - Modify or create a custom prompt template to better align with your content type.


### Getting Help
If you encounter issues:
1. Check the console output for error messages.
2. Ensure all dependencies are installed correctly.
3. Verify that your API key and WordPress credentials are valid.


## Contribution Guidelines
Contributions to this project are welcome! You can participate by:
1. Reporting bugs or suggesting new features via Issues.
2. Submitting Pull Requests to improve code quality.
3. Adding new prompt templates for different content types.
4. Enhancing project documentation.


## License
This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.


## Changelog

### v1.1.0 (2025-08-31)
- Added AI Formatting Optimization Module
- Implemented configurable OpenAI parameters
- Added custom prompt template system
- Added optimization intensity control


### v1.0.0 (2025-09-01)
- Initial release
- Supports manual input of HTML content
- Allows configuration of article status, categories, tags, and excerpts
- Added pre-publishing confirmation mechanism


---
For questions or suggestions, please provide feedback via Issues or contact the developer.