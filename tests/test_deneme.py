import time
import undetected_chromedriver as uc  # Undetected ChromeDriver kullanımı

# Chrome seçeneklerini belirleme
options = uc.ChromeOptions()
options.add_argument("--no-sandbox")
options.add_argument("--disable-blink-features=AutomationControlled")

# Undetected ChromeDriver başlatma
driver = uc.Chrome(options=options)

# WebDriver'in tespit edilmemesi için stealth benzeri özellikler ekleme
driver.execute_script(
    "Object.defineProperty(navigator, 'webdriver', {get: () => undefined})"
)

# URL'yi açma
url = "https://app.forceget.com/system/account/register"
driver.get(url)

# Sayfanın yüklenmesi ve CAPTCHA için bekleme süresi
time.sleep(10)

# Tarayıcıyı kapatma
driver.quit()