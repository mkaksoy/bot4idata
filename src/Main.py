import undetected_chromedriver as uc
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import time
import os
import random

def wait_random(min_sec=1.3, max_sec=4.8):
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
    log("Site: https://www.idata.com.tr/ita/tr")
    driver.get('https://www.idata.com.tr/ita/tr')
    wait_random()
finally:
    wait_random()
    log("Closing browser...")
    driver.quit()
