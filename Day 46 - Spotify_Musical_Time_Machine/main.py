# Travel to time and listen top hits from that period
# Program creates Spotify playlist with 100 songs which were on top at particular date
# Specify any date and enjoy your playlist 🎵
# Spotify account needed
import os
import requests
import spotipy
from bs4 import BeautifulSoup
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv
load_dotenv()

SP_CLIENT_ID = os.getenv('SPOTIFY_CLIENT_ID')
SP_CLIENT_SECRET = os.getenv('SPOTIFY_CLIENT_SECRET')

date = input("What year do you want to travel to 🎵 ? Type the date in this format YYYY-MM-DD: ")

URL = f"https://www.billboard.com/charts/hot-100/{date}/"
response = requests.get(URL)
website = response.text

soup = BeautifulSoup(website, "html.parser")

all_songs = soup.find_all(name="span", class_="chart-element__information__song")
songs = [song.getText() for song in all_songs]

# Spotify Authentication
sp = spotipy.Spotify(
    auth_mg = SpotifyOAuth(
        scope= "playlist-modify-private",
        redirect_uri= URL,
        client_id= SP_CLIENT_ID,
        client_secret= SP_CLIENT_SECRET,
        show_dialog= True,
        cache_path= "token.txt"
    )
)

user_id = sp.current_user()["id"]
print(f"USER ID: {user_id}") 

# Create Playlist
song_uris = []
year = date.split("-")[0]
for song in songs:
    res = sp.search(q=f"track:{song} year:{year}", type="track")
    print(f"Search result: {res}")
    try:
        uri = res["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. [Skipped]")

playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False)
print(f"Playlist: {playlist}")

sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)