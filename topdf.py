from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from PIL import Image
import time
import sys
sys.stdout.reconfigure(encoding='utf-8')


# ======== BƯỚC 1: CẤU HÌNH SELENIUM CHROME HEADLESS ========
chrome_options = Options()
chrome_options.add_argument("--headless=new")  # Chrome 109+ cần flag này
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--window-size=1920,1080")

driver = webdriver.Chrome(options=chrome_options)

try:
    # ======== BƯỚC 2: ĐĂNG NHẬP SUPERSET ========
    print("🔐 Đang đăng nhập Superset...")
    driver.get("http://localhost:8088/login/")
    time.sleep(2)

    driver.find_element("name", "username").send_keys("admin")
    driver.find_element("name", "password").send_keys("admin")
    driver.find_element("tag name", "form").submit()
    time.sleep(5)

    # ======== BƯỚC 3: TRUY CẬP DASHBOARD VÀ CHỜ LOAD ========
    print("📊 Đang truy cập dashboard...")
    dashboard_url = "http://localhost:8088/superset/dashboard/1/?native_filters_key=L1QhxvzMdOkxS58ecLPcCtrGsUlwrX_4e4WvzhLeVAHjDTPnnKaup8OS9PNf1Mta"
    driver.get(dashboard_url)
    time.sleep(8)  # Tùy dashboard mà tăng nếu render chậm

    # ======== BƯỚC 4: CHỤP ẢNH TOÀN TRANG ========
    scroll_height = driver.execute_script("return document.body.scrollHeight")
    driver.set_window_size(1920, scroll_height)
    time.sleep(2)

    screenshot_path = "dashboard_full.png"
    driver.save_screenshot(screenshot_path)
    print(f"✅ Đã chụp ảnh toàn trang: {screenshot_path}")

    # ======== BƯỚC 5: CHUYỂN PNG → PDF ========
    print("📄 Đang chuyển ảnh sang PDF...")
    image = Image.open(screenshot_path)
    if image.mode == "RGBA":
        image = image.convert("RGB")

    pdf_path = "dashboard_full.pdf"
    image.save(pdf_path, "PDF", resolution=100.0)
    print(f"✅ Đã tạo PDF: {pdf_path}")

finally:
    driver.quit()