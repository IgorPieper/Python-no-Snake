from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/")
content = response.text

soup = BeautifulSoup(content, "html.parser")
response = soup.find_all("a", class_="titlelink")
span = soup.find_all("span", class_="score")

articles = {}

for n in range(0, len(response)-1):
    articles = {n: {"title": response[n].text, "link": response[n]['href'], "points":span[n].text.split()[0]}}
    print(articles)
