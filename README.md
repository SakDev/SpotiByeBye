# SpotiByeBye
## How it works
The program detects when an advertisement plays by monitoring the type of the track that is currently playing, using the Spotipy API. 
When an ad is detected, the program restarts Spotify by the os module and plays it via pynput.

## Setting up the Spotify API
1. Go to https://developer.spotify.com/dashboard and sign in with your Spotify account.
2. Click on the 'CREATE AN APP' option and provide an app name and app description as you'd like.
3. Go to 'EDIT SETTINGS' and exactly fill in the Redirect URIs placeholder with https://www.google.com/, and click on Save.
4. Copy the Client ID and Client Secret and paste it in the corresponding place holders in ByeAds.py.

