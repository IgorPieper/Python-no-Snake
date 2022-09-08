from bs4 import BeautifulSoup
import requests

import spotipy
from spotipy.oauth2 import SpotifyOAuth

C_ID = "Your ID"
C_SECRET = "Your Secret"

# -------------------------- Web Scraping ---------------------------------- #

date = input("Which year do you want to travel to? (YYYY-MM-DD): ")
link = "https://www.billboard.com/charts/hot-100/" + date + "/"

response = requests.get(link)
content = response.text

soup = BeautifulSoup(content, "html.parser")
response = soup.select("li ul li h3")

list = []

for n in response:
    list.append(n.text.lstrip())

new_list = []

for n in list:
    n = n.replace("\n", "").replace("\t", "")
    new_list.append(n)

# -------------------------- Spotify API ---------------------------------- #

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id=C_ID,
        client_secret=C_SECRET,
        show_dialog=True,
        cache_path="token.txt"
    )
)
user_id = sp.current_user()["id"]

year = date.split("-")[0]
song_uris = []

for song in new_list:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped")

playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False)

sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)
