from selenium import webdriver
from selenium.webdriver.common.by import By
import time

chrome_driver = "C:\Development\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver)
driver.get("http://orteil.dashnet.org/experiments/cookie/")

cookie = driver.find_element(by="xpath", value='//*[@id="cookie"]')

timeout = time.time() + 1

while True:
    cookie.click()
    if time.time() > timeout:
        timeout = time.time() + 1
        money = driver.find_element(by="xpath", value='//*[@id="money"]')
        money = int(money.text.replace(",", ""))
        item_prices = []
        item_cost = []
        item_names = []
        upgrade = driver.find_elements(By.CSS_SELECTOR, "#store b")
        for n in range(0, len(upgrade)-1):
            item_names.append(upgrade[n].text.split("-")[0])
            item_prices.append(upgrade[n].text.split("-")[1])
        item_names.reverse()
        for n in item_prices:
            item_cost.append(int(n.replace(",", "")))
        item_cost.reverse()
        for n in range(0, len(item_cost)):
            if item_cost[n] <= money:
                try:
                    print(f"buy{item_names[n].capitalize().rstrip()}")
                    buy = driver.find_element(By.ID, f"buy{item_names[n].capitalize().rstrip()}")
                    money = driver.find_element(by="xpath", value='//*[@id="money"]')
                    money = int(money.text.replace(",", ""))
                    buy.click()
                except:
                    pass
