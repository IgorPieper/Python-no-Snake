from selenium import webdriver

chrome_driver = "C:\Development\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver)
driver.get("https://www.python.org/")

events = driver.find_element(by="xpath", value='//*[@id="content"]/div/section/div[2]/div[2]/div/ul')

event_list = {}
element = events.text.split("\n")
number = 0

for n in range(0, len(element)):
    if n % 2 == 0:
        event_list[number] = {"date": element[n], "text": element[n+1]}
        number += 1

print(event_list)
