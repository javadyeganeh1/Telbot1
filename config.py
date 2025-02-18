import os

class Config:
    # Telegram
    BOT_TOKEN = os.getenv("TELEGRAM_API_TOKEN", "7785178055:AAEplGGnh0GiM6hoHlTJ8z0_J5OJoeUKU0A")
    TEMP_DIR = "temp"
    RATE_LIMIT = 1.5  # seconds between requests
    
    # Chrome
    CHROME_OPTIONS = [
        "--headless",
        "--no-sandbox",
        "--disable-dev-shm-usage",
        "--disable-gpu",
        "--window-size=1920,1080",
        "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    ]
    CHROME_DRIVER_PATH = "/usr/bin/chromedriver"
    CHROME_BINARY_PATH = "/usr/bin/google-chrome"
    
    # Messages
    WELCOME_MESSAGE = """
    🤖 *ربات اینستاگرام پیشرفته*
    
    ✨ امکانات ربات:
    • دانلود پست، ریلیز و استوری
    • نمایش اطلاعات کامل پروفایل
    • پشتیبانی از محتوای HD
    
    🔍 برای شروع از دکمه‌های زیر استفاده کنید:
    """
    
    DOWNLOAD_INSTRUCTION = """
    🔗 لینک پست اینستاگرام را ارسال کنید:
    • پست‌های ساده: https://www.instagram.com/p/...
    • ریلیز: https://www.instagram.com/reel/...
    • استوری: https://www.instagram.com/stories/...
    """
    
    PROFILE_INSTRUCTION = """
    📌 نام کاربری اینستاگرام را وارد کنید:
    مثال: instagram
    """
