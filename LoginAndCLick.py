from selenium import webdriver
from selenium.webdriver.common.by import By
import time
def get_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("disable-infobars")
    options.add_argument("start-maximized")
    options.add_argument("disable-dev-shm-usage")
    options.add_argument("no-sandbox")
    options.add_experimental_option("excludeSwitches",["enable-automation"])
    options.add_argument("disable-blink-features=AutomationControlled")

    driver = webdriver.Chrome(options=options)
    # https://automated.pythonanywhere.com

    driver.get("https://automated.pythonanywhere.com")
    return driver

def main():
    driver = get_driver()
    time.sleep(2)
    driver.find_element(By.ID, value="id_password").send_keys("automated")
    time.sleep(2)
    driver.find_element(By.ID, value="id_password").send_keys("automatedautomated" + Keys.RETURN)
    time.sleep(2)
    driver.find_element(By.XPATH, value="/html/body/nav/div/a").click()
    time.sleep(2)
    dynamic_element = driver.find_element(By.ID, value="displaytimer")
    return clean_text(dynamic_element.text)

 print(main())