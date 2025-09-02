# Cross-Platform WordPress Auto-Publisher (Python + Flutter)

A **cross-platform tool** for auto-publishing articles to WordPress via the WordPress REST API, supporting both **PC (Python)** and **Android (Flutter)**. The Python client includes AI-powered content formatting, while the Flutter client offers out-of-the-box usage on Android devices—combining flexibility for desktops and portability for mobile.


## ✨ Key Features

### 🔹 Python Client (PC)
- **WordPress Article Publishing**: Auto-publish content to WordPress via REST API.
- **HTML & Markdown Support**: Manually input content in HTML or Markdown format.
- **AI-Powered Formatting**: Integrate OpenAI GPT models to optimize content structure and readability.
- **Flexible Configuration**: Centralized settings (via `config.py`), with support for custom prompt templates.
- **Interactive CLI**: User-friendly command-line interface with clear step-by-step prompts.
- **Robust Error Handling**: Detailed error messages and exception catching for easy troubleshooting.

### 🔹 Flutter Client (Android)
- **Android Out-of-the-Box Usage**: Install the APK and use immediately—no extra setup required.
- **Clean Visual UI**: Android-optimized interface with two core screens: *Configuration* and *Publishing*.
- **Local Config Persistence**: Save WordPress credentials securely via `SharedPreferences` (no repeated input).
- **Core Publishing Features**: Input article title, HTML content, and select publish status (Draft/Publish).
- **Optional Fields Support**: Configure category IDs, tag IDs, and article excerpts.
- **Real-Time Feedback**: Clear success/failure notifications, with direct links to view published articles.


## 📁 Project Structure

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


## 🛠️ Installation & Setup

### 🔹 Python Client (PC)

#### Prerequisites
- Python 3.6+
- WordPress 5.6+ (must support "Application Passwords" feature)
- OpenAI API account (required for AI formatting)

#### Installation Steps
1. Navigate to the `python-branch` directory:
   ```bash
   cd python-branch
   ```
2. Install dependencies:
   ```bash
   pip install -r ../requirements.txt
   ```
3. Configure `config.py`:
   - **WordPress Settings**: Add your site URL, username, and application password.
   - **OpenAI Settings (Optional)**: Enter your API key and select a default model (e.g., `gpt-3.5-turbo`).
   - **Prompt Templates (Optional)**: Customize prompts for AI formatting.
4. Generate a WordPress Application Password:
   - Log into your WordPress admin → Go to **Users → Profile**.
   - Scroll to **Application Passwords** → Enter an app name (e.g., "Python Publisher") → Click **Generate**.
   - Copy the 16-character password (format: `xxxx xxxx xxxx xxxx`) and paste it into `config.py` as `APP_PASSWORD`.


### 🔹 Flutter Client (Android)

#### Prerequisites
- Flutter 3.0+ (for development only; end-users need just the APK)
- Android device/emulator (Android 5.0+, API Level 21+)
- Compiled Flutter APK (ready for installation)

#### Installation (End-Users: No Dev Env Needed)
1. Get the Flutter APK:
   - Locate the release APK in `flutter-branch/build/app/outputs/apk/release/app-release.apk`.
2. Install on your Android device:
   - Transfer the APK to your device → Tap to install (enable "Unknown Sources" if prompted).
3. First-Time Setup (Android):
   - Open the app → You’ll be directed to the **Configuration Screen** automatically.
   - Enter:
     - WordPress Site URL (e.g., `https://your-wordpress-site.com` — include `https://`).
     - WordPress username.
     - WordPress Application Password (same as the Python client).
   - Tap **Save Config** → The app will validate credentials and redirect to the **Publishing Screen**.

#### Development Setup (For Customization)
1. Navigate to the `flutter-branch` directory:
   ```bash
   cd flutter-branch
   ```
2. Install Flutter dependencies:
   ```bash
   flutter pub get
   ```
3. Android-Specific Config:
   - Ensure internet permission is added to `android/app/src/main/AndroidManifest.xml`:
     ```xml
     <uses-permission android:name="android.permission.INTERNET" />
     ```
4. Build the release APK:
   ```bash
   flutter build apk --release
   ```


## 🚀 Usage Guide

### 🔹 Python Client (PC)

#### Basic Usage
1. Run the main script:
   ```bash
   cd python-branch
   python main.py
   ```
2. Follow the CLI prompts to input:
   - Article title (required).
   - HTML content (enter `:END` on a new line to finish — required).
   - Whether to use AI formatting (type `y`/`n` — optional).
   - Publish status (`1` = Publish, `2` = Draft — default: Draft).
   - Category IDs/Tag IDs (comma-separated for multiples — optional).
   - Article excerpt (optional).
3. Confirm the details → The tool will send the request to WordPress and return a success/failure status.

#### AI-Powered Formatting (Python-Only)
When you select "Use AI Formatting":
1. Choose a prompt template (e.g., Standard/Technical/Creative).
2. Adjust temperature (0.0–1.0; higher = more creative, default = 0.7).
3. Set max tokens (limits AI response length, default = 1000).
4. Preview the original vs. optimized content → Choose whether to use the optimized version.


### 🔹 Flutter Client (Android)

#### Configure WordPress Credentials
1. Open the app → First launch directs you to the **Configuration Screen**.
2. Enter your WordPress site URL (full and valid, e.g., `https://blog.example.com`).
3. Input your WordPress username and application password.
4. Tap **Save Config** → If valid, you’ll jump to the **Publishing Screen**.
   - To edit config later: Tap the ⚙️ (Settings) icon in the top-right corner.

#### Publish an Article
1. On the **Publishing Screen**, enter:
   - **Article Title** (required — cannot be empty).
   - **Article Content** (HTML format, e.g., `<p>Your content here</p>` — required).
   - **Publish Status** (select "Draft" or "Publish Now").
   - **Category IDs** (optional; comma-separated, e.g., `1,3`).
   - **Tag IDs** (optional; same format as categories).
   - **Article Excerpt** (optional).
2. Tap the bottom button (labeled "Save as Draft" or "Publish Now"):
   - **Success**: A dialog shows the article ID and view link. Tap "View Article" to open it in your browser.
   - **Failure**: A notification explains the issue (e.g., invalid credentials, network error).


## 🔧 Advanced Usage

### 🔹 Python Client Advanced Tips
#### Use the AI Formatter as a Standalone Module
Import `ai_formatter.py` into other Python projects to optimize text:
```python
from ai_formatter import optimize_content

# Original content
original_content = "This is a technical article that needs better structure and readability..."
# Optimize content
optimized_content = optimize_content(
    original_content,
    prompt_template="technical",  # Use technical documentation template
    temperature=0.6,              # Lower creativity for precision
    max_tokens=1500               # Increase response length limit
)

print("Original:", original_content)
print("Optimized:", optimized_content)
```

#### Customize AI Prompt Templates
Edit the `PROMPT_TEMPLATES` dictionary in `python-branch/config.py`:
```python
PROMPT_TEMPLATES = {
    "default": "Optimize this content for readability and professionalism:\n\n{}",
    "technical": "As a technical writer, optimize this content for clarity and accuracy:\n\n{}",
    "seo": "As an SEO expert, optimize this content for readability and keyword density:\n\n{}",  # New SEO template
    "short": "Optimize this content into concise text for mobile reading:\n\n{}"               # New short-text template
}
```


### 🔹 Flutter Client Advanced Tips
#### APK Signing (For App Store Distribution)
To publish the Flutter APK to app stores, configure custom signing:
1. Generate a keystore file (use `keytool` — see [Android docs](https://developer.android.com/studio/publish/app-signing)):
   ```bash
   keytool -genkeypair -alias mykey -keyalg RSA -keysize 2048 -validity 10000 -keystore D:/path/to/your/key.jks
   ```
2. Create `flutter-branch/android/key.properties`:
   ```properties
   keyAlias=mykey
   keyPassword=your-key-password
   storeFile=D:/path/to/your/key.jks
   storePassword=your-keystore-password
   ```
3. Update `flutter-branch/android/app/build.gradle.kts` with signing config (see earlier Flutter setup docs).


## 🐛 Troubleshooting

### 🔹 Python Client Common Issues
1. **OpenAI API Errors**
   - Verify your API key in `config.py` and ensure it has remaining credits.
   - If you see `module 'openai' has no attribute 'error'`, downgrade the OpenAI library:
     ```bash
     pip install openai==0.27.4
     ```

2. **WordPress 401 Unauthorized Error**
   - Confirm your username and application password match (application passwords ≠ login passwords).
   - Ensure your WordPress user has "Publish Posts" permissions.

3. **WordPress API Connection Failures**
   - Double-check your site URL (include `https://` and no trailing slashes).
   - Verify the WordPress REST API works: Visit `https://your-site.com/wp-json/wp/v2/posts` — it should return JSON data.


### 🔹 Flutter Client Common Issues
1. **Config Validation Failures**
   - Ensure your site URL is complete (e.g., `https://blog.example.com` — no typos).
   - Check that your application password is correct (no extra spaces).
   - Verify your Android device has a working internet connection.

2. **APK Installation Failures**
   - Ensure your Android version is ≥ 5.0 (API Level 21).
   - Enable "Unknown Sources" in your device’s security settings.

3. **Network Errors During Publishing**
   - If your WordPress site uses HTTP (not HTTPS), add this to `AndroidManifest.xml` under `<application>`:
     ```xml
     android:usesCleartextTraffic="true"
     ```


## 🤝 Contribution Guidelines
We welcome contributions to this cross-platform project! Here’s how to help:
1. Report bugs or suggest features (open an Issue).
2. Submit Pull Requests to improve code (e.g., UI tweaks, bug fixes, new features).
3. Expand AI prompt templates (Python client).
4. Improve documentation (add examples, clarify steps).


## 📄 License
This project is licensed under the **GNU General Public License**. See the [LICENSE](LICENSE) file for details.


## 📋 Changelog

### v2.0.0 (2025-09-02)
- Added Flutter Android client with out-of-the-box usage.
- Implemented core Flutter features: WordPress config persistence, article publishing, and result feedback.
- Restructured project to separate `python-branch` (PC) and `flutter-branch` (Android).
- Unified WordPress authentication logic across both clients.

### v1.2.0 (2025-09-01)
- Added support for custom OpenAI baseURL configuration.
- Fixed OpenAI library version compatibility issues.
- Improved config management and error handling in the Python client.

### v1.1.0 (2025-09-01)
- Added AI-powered content formatting module to the Python client.
- Added configurable OpenAI parameters (model, temperature, max tokens).
- Implemented custom prompt template system for AI formatting.

### v1.0.0 (2025-08-31)
- Initial release (Python client only).
- Supported manual HTML content input.
- Added options for publish status, categories, tags, and excerpts.
- Implemented pre-publish confirmation step.