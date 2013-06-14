#!/usr/bin/python2.7
# This script is to open browser with token
# Do not forgrt to replace you application ID in address string
# Taras Zakharchenko (c) 2013
import webbrowser
import readline
webbrowser.open('https://oauth.vk.com/authorize?client_id=33242903&scope=docs&redirect_uri=http://oauth.vk.com/blank.html&display=popup&response_type=token');


