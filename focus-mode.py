import sys
import os
from asyncio import subprocess
import subprocess
import pkg_resources

required = {"yt-dlp"}
installed = {pkg.key for pkg in pkg_resources.working_set}
missing = required - installed

if missing:
    # implement pip as a subprocess:
    subprocess.check_call([sys.executable, "-m", "pip", "install", *missing])

import yt_dlp


# Make sure you have Spotify Installed already!
# Also install this if you want to use spotify desktop https://chrome.google.com/webstore/detail/open-spotify-desktop-app/ccilmbdijoknlfpepncnebjkiclplhig/related?hl=en

# Get User Vars
user_profile = os.environ["USERPROFILE"]
try:
    spotify_location = r"{}\AppData\Roaming\Spotify\Spotify.exe".format(user_profile)
except:
    print("Missing Spotify")


# Download gamma with YTL if not existing
url = "https://www.youtube.com/watch?v=894o89TjYFE"
gamma_location = r"{}/Music/gamma.webm".format(user_profile)
ydl_opts = {"format": "bestaudio", "outtmpl": gamma_location}
with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download(url)


# Open both the gamma file and the spotify playlist with first song selected
os.startfile(
    "https://open.spotify.com/track/05ffb3kD0szRIh36eEP12I?context=spotify%3Aplaylist%3A6jux61w7puO9gnNWKQsMwU"
)
os.startfile(gamma_location)
