'''
______________________________________________________________
______________________________________________________________
File:       funksies.py  
Developer:  Ruimteman
Date:       06/08/2023
Description:
    Al die funksies wat ek nodig het om Hangman te speel    
______________________________________________________________
______________________________________________________________
'''

from src.variables import *
import random



def welkom_boodskap():
    print("Welkom by Ruimteman se letter raai")

def kies_letter(counter):
    gekiesde_letter = input("\nKies 'n letter (%i/%i raaie oor): "%(raaie-counter, raaie))
    return gekiesde_letter

def kies_woord():
    while True:
        choice = input("Kies 'n selection mode (1. manual/2. random): ")
        
        if choice == "1":
            while True:
                print(f"\nDie voldengde kategorie is beskikbaar:")
                for index, kategorie in enumerate(lys["Woordelys"], start=1):
                    kat = kategorie["kategorie"]
                    print(f"{index}. {kat}")

                selected_cat = int(input("\nKies 'n katogorie: "))
                selected_category = lys["Woordelys"][selected_cat - 1]["kategorie"]
                print(selected_category)

                # Find the selected category in the list
                category_found = False
                for category in lys["Woordelys"]:
                    if category["kategorie"] == selected_category:
                        category_found = True
                        woord_om_te_raai = random.choice(category["woorde"])
                        print("Katogorie van woord is %s" % (category["kategorie"]))
                        return woord_om_te_raai
            
                if not category_found:
                    print("Daar is nie so katogorie nie! Probeer weer!.")
            
        elif choice == "2":
            while True:
                random_category = random.choice(lys["Woordelys"])
                woord_om_te_raai = random.choice(random_category["woorde"])
                print("Katogorie van woord is %s" % (random_category["kategorie"]))
                return woord_om_te_raai
        
        else:
            print("Daar is nie so mode nie! Kies '1' of '2'.")

def speel(woord, geraaide_letters):
    counter = 0
    letters_verkeerd = ""
    while True:
        l = kies_letter(counter)
        x = 0
        regte_letter = False

        for letter in woord:
            x += 1
            if l == letter:  
                geraaide_letters = geraaide_letters[:x-1] + letter + geraaide_letters[x:]
                regte_letter = True

        if not regte_letter:
            counter += 1
            letters_verkeerd = letters_verkeerd+l

        for letter in geraaide_letters:
            print(letter + " " , end="")

        print("      ----> ",letters_verkeerd , end="")

        if geraaide_letters == woord:
            print("\nJy het gewen!")
            break
        
        if raaie == counter:
            break



    if not geraaide_letters == woord:
        print("\nJy verloor! Die woord was %s"%(woord))
        
def maak_bord(woord):
    geraaide_letters = ""
    for letter in woord:
        print("_ " , end="")
        geraaide_letters = geraaide_letters+"_"
    return geraaide_letters


