import random
import time
import wikipedia
import requests

def player_search():
    player_name=str(input("which player's information do you need?\nPlease write name\n"))
    bio = wikipedia.search(player_name)  # https://wikipedia.readthedocs.io/en/latest/code.html#module-wikipedia
    ans = wikipedia.summary(player_name)
    print(ans) 
    
# i used api from cricapi.com
def upcoming_match():
    match = requests.get('https://cricapi.com/api/matches?apikey=ZVmhKHMQ64NVHLPFXRxuBPKHemy1').json()
    for info in match['matches']:                      
        uni_id = info['unique_id']                 #my api key-ZVmhKHMQ64NVHLPFXRxuBPKHemy1
        team1 = info['team-1']
        team2 = info['team-2']
        date = info['date']
        print(uni_id)
        print(team1)
        print("vs")
        print(team2)
        print(date +"\n")
       # copied from: https://www.cricapi.com/member-test.aspx


def calender():
    api = 'https://cricapi.com/api/matchCalendar?' + 'apikey=ZVmhKHMQ64NVHLPFXRxuBPKHemy1'
    match_info = requests.get(api).json()
    for match in match_info['data']:
        print(match['name'])
        print(match['date'])
        print('\n')
        # copied from: https://www.cricapi.com/member-test.aspx


def old_match():
    match = requests.get('https://cricapi.com/api/cricket?apikey=ZVmhKHMQ64NVHLPFXRxuBPKHemy1').json()
    for info in match['data']:
        uni_id = info['unique_id']
        des = info['description']
        tit = info['title']
        print(uni_id)
        print(des)
        print(tit)
        print("\n")
        # copied from: https://www.cricapi.com/member-test.aspx



def crickbot():
    print("hii")
    time.sleep(1)
    print("i am cricbot")
    time.sleep(1)
    print("How can i help you ?")
    time.sleep(1)
    print("Which type of information do you want from me?")
    time.sleep(1)
    print("1.Bio of player")
    print("2.Information of upcoming matches")
    print("3.Calender of match")
    print("4.Old match")

    while True:
        choice = str(input("Please select your number here\n"))
        if choice == "1" or choice == "a":
            player_search()
        elif choice == "2" or choice == "b":
            upcoming_match()
        elif choice == "3" or choice == "c":
            calender()
        elif choice == "4" or choice == "d":
            old_match()

crickbot()
            