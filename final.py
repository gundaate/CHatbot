from nltk.chat.util import Chat, reflections
import requests
import time
import wikipedia
from datetime import datetime
import selenium.webdriver as webdriver
from selenium.webdriver import *

#log in to cumoodel website
def cumoodel(Username,Password):
    Username=str(input("please input your valid username for\ncumoodel website: "))
    Password = str(input("your password: "))
    print("please be patient :) ")
    url = "https://cumoodle.coventry.ac.uk/"
    # refrance from https://selenium-python.readthedocs.io/getting-started.html#simple-usage
    driver = webdriver.Firefox()
    driver.get(url)
    elem = driver.find_element_by_name("username")
    elem.clear()
    elem.send_keys(Username)#your user name in ""

    em = driver.find_element_by_name("password")
    em.clear()
    em.send_keys(Password)#your password in ""

#facebook login
def facebook(Username,Password):
    Username = str(input("please input your valid username for\nfacebook website: "))
    Password = str(input("your password: "))
    print("please be patient :) ")
    url = "https://en-gb.facebook.com/"
    # refrance from https://selenium-python.readthedocs.io/getting-started.html#simple-usage
    driver = webdriver.Firefox()
    driver.get(url)
    elem = driver.find_element_by_name("email")
    elem.clear()
    elem.send_keys(Username)#your user name in ""

    em = driver.find_element_by_name("pass")
    em.clear()
    em.send_keys(Password)#your password in ""

def weatherRreport(location):
    location=str(input("please type your location to find out\n current weather in pertiular"
                       " location\n::>")+ " weather today")
    print("please be patient :) ")
    # refrance from https://selenium-python.readthedocs.io/getting-started.html#simple-usage
    driver = webdriver.Firefox()
    driver.get("https://www.google.com/search?client=firefox-b-d&q=coventry+weather")
    elem = driver.find_element_by_name("q")
    elem.clear()
    elem.send_keys(location)


# Pairs is a list of patterns and responses.
#refrance from https://www.nltk.org/api/nltk.chat.html#module-nltk.chat
pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, How are you today ?", ]
    ],
    [
        r"(.*)help(.*) ",
        ["I can help you ", ]
    ],
    [
        r"(.*) your name ?",
        ["My name is M.R.N.E.R.D aka Mr.Nerd i am an interactive chat bot", ]
    ],
    [
        r"how are you ?",
        ["I'm doing very well\nHow about You ?", ]
    ],
    [
        r"sorry (.*)",
        ["Its alright", "Its OK, never mind that", ]
    ],
    [
        r"i'm (.*) doing good",
        ["Nice to hear that", "Alright, great !", ]
    ],
    [
        r"(hi|hey|hello|hola|holla)(.*)",
        ["Hello", "Hey there", ]
    ],
    [
        r"what (.*) want ?",
        ["Make me an offer I can't refuse", ]

    ],
    [
        r"(.*) created ?",
        ["Team nerd created me using Python's NLTK library ", "top secret ;)", ]
    ],
    [
        r"(.*) (location|city) ?",
        ['Tokyo, Japan', ]
    ],
    [
        r"how is the weather in (.*)?",
        ["Weather in %1 is amazing like always", "It's hot here in %1", "It's chilli here"
                                                                        " in %1",
         "In %1 there is a 50% chance of rain", ]
    ],
    [
        r"i work (in|at) (.*)?",
        ["%1 is an amazing company, I have heard about it.", ]
    ],
    [
        r"(.*)raining in (.*)",
        ["No rain in the past 4 days here in %2", "In %2 there is a 50% chance of rain", ]
    ],
    [
        r"is it (.*) in (.*)",
        ["No its not %1 in %2", "It could be", "Yes its %1 in %2"]
    ],
    [
        r"how (.*) health (.*)",
        ["Health is very important, but I am a computer, so I don't need to worry about"
         " my health ", ]
    ],
    [
        r"(.*)(sports|game|sport)(.*)",
        ["I'm a very big fan of Basketball", ]
    ],
    [
        r"who (.*) sportsperson ?",
        ["Messy", "LeBron", "D-Wade"]
    ],
    [
        r"who (.*) (moviestar|actor|actress)?",
        ["Zendaya"]
    ],
    [
        r"quit",
        ["Bye for now. See you soon :) ", "It was nice talking to you. See you soon :)"]
    ],
]


def NerdBot():
    # default message at the start
    print("Hi, I'm  M.R.N.E.R.D and I want to help and chat with you ! \nPlease type"
          " lowercase English language to start a conversation. Type quit to leave ")
    # default message at the start
    chat = Chat(pairs, reflections)
    chat.converse()#refrance from https://www.nltk.org/api/nltk.chat.html#module-nltk.chat


# Run the chatbot
def your_choise():
    choice = str(input('\nhi there! \nplease type your option from following: \n1 for '
                       'talking with Mr.Nerd \n2 for log in to cumoodel website '
                       '\n3 for log in to facebook \n4 for live Weather Rreport \n::>'))
    if choice == '1':
        NerdBot()
    elif choice == '2':
        cumoodel(0,0)
    elif choice == '3':
        facebook(0,0)
    elif choice == '4':
        weatherRreport(0)


while True:
    your_choise()


