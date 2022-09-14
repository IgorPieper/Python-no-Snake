from selenium import webdriver
import time

# ------------------- YOUR DATA -------------------------- #

EMAIL = "yourmail@mail.com"
PASS = "yourPASSWORD"
NUMBER = "111111111"

JOB_XPATH = '/html/body/div[5]/div[3]/div[4]/div/div/main/div/section[1]/div/ul/li[2]/div/div[1]'

# ------------------- OPEN LINKEDIN -------------------------- #

LINK = "https://www.linkedin.com/jobs/search/?f_LF=f_AL&geoId=102257491&keywords=python%20developer&location=London%2C%20England%2C%20United%20Kingdom&redirect=false&position=1&pageNum=0"
chrome_driver = "C:\Development\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver)
driver.get(LINK)

# ------------------- LOG IN -------------------------- #

log_in = driver.find_element(by="xpath", value='/html/body/div[3]/header/nav/div/a[2]')
log_in.click()

email_input = driver.find_element(by="xpath", value='/html/body/div/main/div[3]/div[1]/form/div[1]/input')
email_input.send_keys(EMAIL)
pass_input = driver.find_element(by="xpath", value='/html/body/div/main/div[3]/div[1]/form/div[2]/input')
pass_input.send_keys(PASS)

logg = driver.find_element(by="xpath", value='/html/body/div/main/div[3]/div[1]/form/div[3]/button')
logg.click()

# ------------------- FIND INTERESTING JOB -------------------------- #

job = driver.find_element(by="xpath", value=JOB_XPATH)
job.click()

time.sleep(5)

# ------------------- APPLAY -------------------------- #

fast_apply = '/html/body/div[5]/div[3]/div[4]/div/div/main/div/section[2]/div/div[2]/div[1]/div/div[1]/div/div[1]/div[1]/div[3]/div/div/div/button'
apply = driver.find_element(by="xpath", value=fast_apply)
apply.click()

number_input = driver.find_element(by="xpath", value='/html/body/div[3]/div/div/div[2]/div/div[2]/form/div/div/div[3]/div[2]/div/div/input')
number_input.send_keys(NUMBER)

next_first = driver.find_element(by="xpath", value='/html/body/div[3]/div/div/div[2]/div/div[2]/form/footer/div[2]/button')
next_first.click()

next_second = driver.find_element(by="xpath", value='/html/body/div[3]/div/div/div[2]/div/div[2]/form/footer/div[2]/button[2]')
next_second.click()
