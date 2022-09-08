from bs4 import BeautifulSoup
import requests
import lxml
import smtplib

# ------------------------ Web Scraping --------------------- #

link = "https://www.amazon.pl/LEGO-Obi-Wan-75334-element%C3%B3w-urodziny/dp/B09QFPBDKQ/ref" \
       "=pd_rhf_d_se_s_pd_sbs_rvi_sccl_1_2/257-1335247-1397840?pd_rd_w=Q7Kyw&content-id=amzn1.sym.7e388ef7-24ae-41e5" \
       "-80e7-9e03eb3cdeaa&pf_rd_p=7e388ef7-24ae-41e5-80e7-9e03eb3cdeaa&pf_rd_r=ZAV89DQYHVMQ2X5RBC7W&pd_rd_wg=SoXw5" \
       "&pd_rd_r=9a0f419f-2eb0-49f3-b84e-9b5a61b15179&pd_rd_i=B09QFPBDKQ&psc=1 "

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:104.0) Gecko/20100101 Firefox/104.0",
    "Accept-Language": "pl,en-US;q=0.7,en;q=0.3",
}

response = requests.get(link, headers=headers)
content = response.text

soup = BeautifulSoup(content, "lxml")

price = soup.find("span", class_="a-offscreen")
price = float(price.text.replace("zł", "").replace(",", "."))

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
