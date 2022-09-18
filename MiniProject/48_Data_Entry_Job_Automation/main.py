from bs4 import BeautifulSoup
from selenium import webdriver
import requests
import time

# -------------- CONS ---------------- #

OFFERS_PAGE = 'https://www.zillow.com/san-francisco-ca/rentals/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22mapBounds%22%3A%7B%22north%22%3A37.850839428243134%2C%22east%22%3A-122.30627704076616%2C%22south%22%3A37.630384847338306%2C%22west%22%3A-122.70796466283647%7D%2C%22mapZoom%22%3A12%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%7D%2C%22isListVisible%22%3Atrue%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A20330%2C%22regionType%22%3A6%7D%5D%7D'
CHROME_DRIVER = ""
FORMS_PAGE = ''

# -------------- Connecting ---------------- #

headers = {
    "User-Agent": "",
    "Accept-Language": "",
}

response = requests.get(OFFERS_PAGE, headers=headers)
content = response.text

# --------------- Data Taking --------------- #

soup = BeautifulSoup(content, "html.parser")
links = []
true_links = []
address = []
price = []

for n in soup.find_all(class_="property-card-link"):
    if n["href"] not in links:
        links.append(n["href"])

for n in soup.find_all("address"):
    address.append(n.text)

for n in soup.find_all(class_="StyledPropertyCardDataArea-c11n-8-69-2__sc-yipmu-0"):
    if n.span:
        if n.span.text[0] == "$":
            price.append(n.span.text)

for n in links:
    if n[0] != "h":
        true_links.append(f"https://www.zillow.com{n}")
    else:
        true_links.append(n)

for n in range(0, len(links)):
    print(f"{true_links[n]}, {address[n]}, {price[n]}")

# --------------- Data Sending --------------- #

driver = webdriver.Chrome(executable_path=CHROME_DRIVER)
driver.get(FORMS_PAGE)

time.sleep(3)

for n in range(0, len(links)):
    address_input = driver.find_element(by="xpath", value='/html/body/div/div[2]/form/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    price_input = driver.find_element(by="xpath", value="/html/body/div/div[2]/form/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input")
    link_input = driver.find_element(by="xpath", value="/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input")
    submit_button = driver.find_element(by="xpath", value='/html/body/div/div[2]/form/div[2]/div/div[3]/div[1]/div[1]/div/span')
    
    address_input.send_keys(address[n])
    price_input.send_keys(price[n])
    link_input.send_keys(true_links[n])
    submit_button.click()
    time.sleep(2)
    again_button = driver.find_element(by="xpath", value="/html/body/div[1]/div[2]/div[1]/div/div[4]/a")
    again_button.click()
