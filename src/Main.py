import undetected_chromedriver as uc
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import os
import random

def wait_random(min_sec=5.3, max_sec=7.8):
    t = random.uniform(min_sec, max_sec)
    print(f"[LOG] Bekleniyor: {t:.2f} saniye...")
    time.sleep(t)

def log(msg):
    print(f"[LOG] {msg}")

# Setup
log("Starting Chrome...")
service = Service(executable_path=os.path.abspath("../public/chromedriver.exe"))

options = Options()
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36")

driver = uc.Chrome(options=options, service=service)

try:
    i = str() # (i)nput
    while i != "exit":
        i = input("Enter command (type help for commands):")

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
            driver.get("https://www.idata.com.tr/ita/tr/p/randevu-islemleri-ita")  # IP anlaşıldıktan sonra artık vize alım sayfasına girilebilir.
            # İşlemler burada yapılacak

        elif i == ("pause" or "resume"):
            log("Coming soon...")
        else:
            log("Invalid command. Type help for commands.")
finally:
    log("Program has finished running.")
    log("Closing browser...")
    driver.quit()
