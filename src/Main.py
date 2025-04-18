import undetected_chromedriver as uc
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import os
import random
import atexit
import base64
import re

def wait_random(min_sec=5.3, max_sec=7.8):
    t = random.uniform(min_sec, max_sec)
    print(f"[LOG] Bekleniyor: {t:.2f} saniye...")
    time.sleep(t)

def log(msg):
    print(f"[LOG] {msg}")

driver = None

def safe_quit():
    global driver
    if driver:
        try:
            log("Safely closing browser...")
            driver.quit()
        except Exception as e:
            log(f"Error closing browser: {e}")
            try:
                driver.service.process.kill()
            except:
                pass

atexit.register(safe_quit)


# Function to handle base64 image data
def save_base64_image(data_url, save_path):
    if data_url.startswith('data:image/'):
        base64_data = data_url.split(',')[1]

        with open(save_path, 'wb') as f:
            f.write(base64.b64decode(base64_data))
        return True
    else:
        return False


try:
    # Setup
    log("Starting Chrome...")
    service = Service(executable_path=os.path.abspath("../public/chromedriver.exe"))

    download_dir = os.path.abspath("../auto/")
    os.makedirs(download_dir, exist_ok=True)

    options = uc.ChromeOptions()
    options.add_argument(
        "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36")

    prefs = {
        "download.default_directory": download_dir,
    }
    options.add_experimental_option("prefs", prefs)

    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    driver = uc.Chrome(options=options, service=service)

    window_width = 800
    window_height = 600

    driver.set_window_size(window_width, window_height)

    i = str()  # (i)nput
    while i != "exit":
        i = input("Enter command (type help for commands): ")

        if i == "exit":
            log("Terminating program...")
            break
        elif i == "help":
            log("Available commands:\nexit: Stop the bot\nhelp: Get help\nstart: Start the bot\npause: Pause the bot\nresume: Resume the bot")
        elif i == "start":
            log("Site: https://www.idata.com.tr/ita/tr")
            driver.get('https://www.idata.com.tr/ita/tr')
            driver.maximize_window()
            # Ekran büyütülüyor, Cloudflare JavaScript çalışmasına izin vermediği için şimdilik işlem yok.
            wait_random()
            if "iDATA" in driver.title:
                log("Bypassed Cloudflare successfuly!")
            else:
                log("Cloudflare blocked the request. Try again later.")
                continue
            driver.get(
                "https://it-tr-appointment.idata.com.tr/tr")  # IP anlaşıldıktan sonra artık vize alım sayfasına girilebilir.
            # İşlemler burada yapılacak

            try:
                captcha = driver.find_elements(By.CLASS_NAME, "imageCaptcha")[0]
                captcha_url = captcha.get_attribute("src")
                log(f"Found captcha with data URL format")

                # Save the base64 image
                captcha_path = os.path.join(download_dir, "captcha.png")
                if save_base64_image(captcha_url, captcha_path):
                    log(f"Captcha saved to: {captcha_path}")
                else:
                    log(f"Failed to save captcha - unexpected format: {captcha_url[:30]}...")

            except Exception as e:
                log(f"Error handling captcha: {str(e)}")

        elif i in ["pause", "resume"]:
            log("Coming soon...")
        else:
            log("Invalid command. Type help for commands.")

except Exception as e:
    log(f"An error occurred: {str(e)}")

finally:
    pass