from selenium import webdriver

chrome_driver = "C:\Development\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver)
driver.get("http://secure-retreat-92358.herokuapp.com/")

first = driver.find_element(by="xpath", value='/html/body/form/input[1]')
second = driver.find_element(by="xpath", value='/html/body/form/input[2]')
third = driver.find_element(by="xpath", value='/html/body/form/input[3]')
submit = driver.find_element(by="xpath", value='/html/body/form/button')

first.send_keys("Yes")
second.send_keys("No")
third.send_keys("you_know@gmail.com")
submit.click()
