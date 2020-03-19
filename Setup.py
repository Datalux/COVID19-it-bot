# -*- coding: utf-8 -*-
import json, sys

class Setup:
    __token__ = ""
    __channel__ = ""
    __time__ = 0


    def __init__(self):
        with open("config.json", "r") as r:
            try:
                setup = json.load(r)

                if setup['time'] > 0:
                    self.__time__ = setup['time']
                else:
                    print("Errore. Il valore time non può essere negativo")

                self.__token__ = setup['token']
                self.__channel__ = setup['channel']

            except:
                print("Errore. Assicurati che non ci siano errori nel file.")
                sys.exit(0)

    def get_token(self):
        return self.__token__

    def get_time(self):
        return self.__time__

    def get_channel(self):
        return self.__channel__
        
