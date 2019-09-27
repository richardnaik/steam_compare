# Quick and dirty script to compare two Steam libraries and return all shared games

import sys
import requests
import json
#from sets import Set

steamid_1 = sys.argv[1]
steamid_2 = sys.argv[2]
api_key = sys.argv[3]

r1 = requests.get('http://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/?key='+api_key+'&steamid='+steamid_1+'&format=json&include_appinfo=1')
library_1 = []
for element in r1.json()["response"]["games"]:
    library_1.append(element["name"])
library_1 = set(library_1)

r2 = requests.get('http://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/?key='+api_key+'&steamid='+steamid_2+'&format=json&include_appinfo=1')
library_2 = []
for element in r2.json()["response"]["games"]:
    library_2.append(element["name"])
library_2 = set(library_2)

common_games = library_1.intersection(library_2)
for element in sorted(common_games):
    print(element)

