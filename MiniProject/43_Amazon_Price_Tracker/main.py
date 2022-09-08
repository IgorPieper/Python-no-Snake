from bs4 import BeautifulSoup
import requests
import lxml
import smtplib

# ------------------------ Web Scraping --------------------- #

link = "Amazon product link"

headers = {
    "User-Agent": "complete",
    "Accept-Language": "complete",
}

response = requests.get(link, headers=headers)
content = response.text

soup = BeautifulSoup(content, "lxml")

price = soup.find("span", class_="a-offscreen")
price = float(price.text.replace("zł", "").replace(",", ".")) #change zł into your currency

product_name = soup.find(id="productTitle")
product_name = product_name.text.lstrip()

# ------------------------ Mail Sending --------------------- #

my_email = "yourmail@mail.com"
password = "haslo1234"
location = "smtp.mail.com"

if price < 150:
    with smtplib.SMTP(location) as connect:
        connect.starttls()
        connect.login(user=my_email, password=password)
        connect.sendmail(
            from_addr=my_email,
            to_addrs="someonemail@mail.com",
            msg=f"Subject:Super Offer\n\n{product_name} for only {price}. \n Here is your link: {link}"
        )
else:
    print("Not yet")
