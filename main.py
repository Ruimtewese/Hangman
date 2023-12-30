'''
______________________________________________________________
______________________________________________________________
File:       main.py  
Developer:  Ruimteman
Date:       06/08/2023
Description:
    Hangman game  
______________________________________________________________
______________________________________________________________
'''

from src.funksies import *
from src.variables import *



welkom_boodskap() # laai die welkom boodskap

while True:
    woord = kies_woord() # kies 'n random woord uit die lys

    a =  maak_bord(woord)   # maak die eerste skoon bord
    speel(woord, a) # speel die rondtes wat nodig is om die bord op te los

    # vra die speler of hy nog 'n rondte wil speel
    speel_verder = input("Wil jy nog 'n rondte speel? (J/N): ").upper()
    if speel_verder == "N":
        break         
               

            

  


    
            

