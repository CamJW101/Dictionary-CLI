#!/usr/bin/env python3
import requests
import sys
import json 
definition = requests.get('https://api.dictionaryapi.dev/api/v2/entries/en/'+sys.argv[1].replace('\n',''))
try:
    if(definition.json()[0]["meanings"][0]["definitions"][1]['definition'] is not None):
        if(input("There are multiple definitions of this word, display them all? (Y/N)").upper() == "Y"):
            index = 0
            for item in definition.json()[0]["meanings"][0]["definitions"]:
                print(str(index+1)+': '+str(definition.json()[0]["meanings"][0]["definitions"][index]['definition']))
                index+=1
except IndexError:
   print(str(1)+': '+str(definition.json()[0]["meanings"][0]["definitions"][0]['definition']))
except KeyError:
   print("That is not a valid word in the english dictionary.")