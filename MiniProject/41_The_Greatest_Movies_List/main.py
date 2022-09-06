from bs4 import BeautifulSoup
import requests

response = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
content = response.text

soup = BeautifulSoup(content, "html.parser")
response = soup.find_all("h3", class_="title")
for n in range(0, len(response)):
    print(response[len(response)-n-1].text)
