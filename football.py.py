"https://soccer.sportmonks.com/api/v2.0/livescores/now?api_token=7xgsB80QJW7rw43oHUppSmmweEglNkjKbfFqTCBukA9BFrcLBtlN5eFUyd3h"
import time
import requests
import wikipedia
import random
import webbrowser


def footballmain():
    heading = 'FOOTBALLBOT'
    heading = heading.center(50)  # https://www.tutorialspoint.com/python/string_center.htm

    print("\033[0;30;43m  \n" + heading)  # code copied from:- http://ozzmaker.com/add-colour-to-text-in-python/
    grettings = ["Hi", "Hey", "Hello", "Hiya"]
    print(random.choice(grettings))
    time.sleep(1.5)
    print(" My name is FOOTBALLBOT")
    time.sleep(1.5)
    while True:
        print("PLEASE SELECT A NUMBER FROM BELOW")
        time.sleep(2.5)

        print('''
                              1- Player information
                              2 - Today's matches
                              3 - Up coming matches
                              4 - Exit
                              ''')

        user_input = int(input("Please select a number \n"))

        if user_input == 1:
            players_name = str(input("Please enter player of your choice's name \n")).upper()
            player_info = wikipedia.summary(players_name)
            print(player_info)

        elif user_input == 2:

            footballPage = webbrowser.open("https://www.livescore.com")

            print(footballPage)

        elif user_input == 3:
            comingGames = webbrowser.open("https://www.livescore.com/soccer/2020-03-21/3 ")
            print(comingGames)

        elif user_input == 4:
            print("THANK YOU VERY MUCH FOR USING FOOTBALLBOT ,I HOPE ALL MY INFORMATION WERE USEFUL.GOD BLESS YOU")
            break

footballmain()