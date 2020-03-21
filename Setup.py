# -*- coding: utf-8 -*-
import json, sys

class Setup:
    __token__ = ""
    __channel__ = ""


    def __init__(self):
        with open("config.json", "r") as r:
            try:
                setup = json.load(r)

                self.__token__ = setup['token']
                self.__channel__ = setup['channel']

            except:
                print("Errore. Assicurati che non ci siano errori nel file.")
                sys.exit(0)

    def get_token(self):
        return self.__token__

    def get_channel(self):
        return self.__channel__
        
