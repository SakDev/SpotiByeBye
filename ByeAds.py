# SpotiByeBye
# by @SakDev (github)

import os
import time
import spotipy
import spotipy.util as util
from pynput.keyboard import Key, Controller

keyboard = Controller()


def closeSpotify():
    os.system("taskkill /f /im spotify.exe")
    time.sleep(0.25)


def openSpotify():
    os.system('spotify.exe')
    time.sleep(0.25)


def playSpotify():
    time.sleep(1.5)
    keyboard.press(Key.media_play_pause)
    keyboard.release(Key.media_play_pause)
    keyboard.press(Key.media_next)
    keyboard.release(Key.media_next)
    time.sleep(2.0)
    keyboard.press(Key.alt_l)
    keyboard.press(Key.tab)
    keyboard.release(Key.alt_l)
    keyboard.release(Key.tab)


def restartSpotify():
    closeSpotify()
    openSpotify()
    playSpotify()


spotifyUsername = "#EnterUsernameHere"
spotifyClientID = "#EnterClientIDHere"
spotifyClientSecret = "#EnterClientSecretHere"
spotifyAccessScope = "user-read-currently-playing user-modify-playback-state"
spotifyRedirectURI = "https://www.google.com/"

def setupSpotifyObject(username, scope, clientID, clientSecret, redirectURI):
    token = util.prompt_for_user_token(username, scope, clientID, clientSecret, redirectURI)
    return spotipy.Spotify(auth=token)


def main():
    global spotifyObject

    try:
        trackInfo = spotifyObject.current_user_playing_track()

    except:
        print("Token Expired")
        spotifyObject = setupSpotifyObject(spotifyUsername, spotifyAccessScope, spotifyClientID, spotifyClientSecret,
                                           spotifyRedirectURI)
        trackInfo = spotifyObject.current_user_playing_track()

    try:
        if trackInfo['currently_playing_type'] == 'ad':
            restartSpotify()
    except TypeError:
        pass

    #use print(trackInfo) here to get live data about the currently playing track


spotifyObject = setupSpotifyObject(spotifyUsername, spotifyAccessScope, spotifyClientID, spotifyClientSecret,
                                   spotifyRedirectURI)

while (True):
    main()
    time.sleep(1)


