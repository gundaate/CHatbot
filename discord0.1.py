import discord
from selenium import webdriver
from bs4 import BeautifulSoup
from nltk.chat.util import Chat, reflections
import requests
import nltk
import time
import random
from discord.ext import commands
from discord.ext.commands import Bot
from discord.voice_client import VoiceClient
import asyncio

#function to get bot token

def read_token():
    with open('token.txt', 'r') as f:     # Opens the text doc in witch bots token is copied into
        lines = f.readlines()             # Reads the text doc token data
        return lines[0].strip()           # Returns token data

token = read_token()                      # Reads read_token functions return value, sets it to var name token
client = discord.Client()                 # Holy prayer of discord(probably a shorting of the function name)

def GoogleSearch(Si):
    driver = webdriver.Chrome()
    driver.get(f'https://www.google.co.uk/search?sxsrf=ALeKk02tim4alhtuAsyOXAvNkCvMFUynNg%3A1583734997273&ei=1eBlXu2oENCFhbIPiIWRgAQ&q={Si}+meaning')
    content = driver.page_source
    soup = BeautifulSoup(content, "html.parser")
    Gname = []
    for a in soup.findAll('div', attrs={'class': 'mw'}):
        gname = a.find('span', attrs={'class': "e24Kjd"})
        Gname.append(gname)

    driver.quit()
    G2name = str(Gname)
    G3name = list(G2name)

    a = 0
    b = 1
    c = 2
    d = 3
    e = 4
    f = 5
    i = 0
    for letter in G3name:
        if G3name[a] == '[' and G3name[b] == 'N' and G3name[c] == 'o' and G3name[d] == 'n' and G3name[e] == 'e' and G3name[f] == ',':
            G3name[a] = ''
            G3name[b] = ''
            G3name[c] = ''
            G3name[d] = ''
            G3name[e] = ''
            G3name[f] = ''
        if G3name[a] == '<' and G3name[b] == 's' and G3name[c] == 'p' and G3name[d] == 'a' and G3name[e] == 'n' and G3name[f] == ' ':
            G3name[a] = ''
            G3name[b] = ''
            G3name[c] = ''
            G3name[d] = ''
            G3name[e] = ''
            G3name[f] = ''
        if G3name[a] == 'c' and G3name[b] == 'l' and G3name[c] == 'a' and G3name[d] == 's' and G3name[e] == 's' and G3name[f] == '=':
            G3name[a] = ''
            G3name[b] = ''
            G3name[c] = ''
            G3name[d] = ''
            G3name[e] = ''
            G3name[f] = ''
        if G3name[a] == '"' and G3name[b] == 'e' and G3name[c] == '2' and G3name[d] == '4' and G3name[e] == 'K' and G3name[f] == 'j':
            G3name[a] = ''
            G3name[b] = ''
            G3name[c] = ''
            G3name[d] = ''
            G3name[e] = ''
            G3name[f] = ''
        if G3name[a] == 'd' and G3name[b] == '"' and G3name[c] == '>' and G3name[d] == ' ':
            G3name[a] = ''
            G3name[b] = ''
            G3name[c] = ''
            G3name[d] = ''
        if G3name[a] == '<' and G3name[b] == 'b' and G3name[c] == '>':
            G3name[a] = ''
            G3name[b] = ''
            G3name[c] = ''
        if G3name[a] == '<' and G3name[b] == '/' and G3name[c] == 'b' and G3name[d] == '>':
            G3name[a] = ''
            G3name[b] = ''
            G3name[c] = ''
            G3name[d] = ''
        if G3name[a] == '<' and G3name[b] == '/' and G3name[c] == 's' and G3name[d] == 'p':
            G3name[a] = ''
            G3name[b] = ''
            G3name[c] = ''
            G3name[d] = ''
        if G3name[a] == 'a' and G3name[b] == 'n' and G3name[c] == '>' and G3name[d] == ']':
            G3name[a] = ''
            G3name[b] = ''
            G3name[c] = ''
            G3name[d] = ''
        if G3name[a] == 'd' and G3name[b] == '"' and G3name[c] == '>':
            G3name[a] = ''
            G3name[b] = ''
            G3name[c] = ''

        a+=1
        b+=1
        c+=1
        d+=1
        e+=1
        f+=1

    for letter in G3name:
        print(G3name[i])
        i+=1

    print(G3name)

    return ''.join(G3name)



@client.event                                        # Setting up a discord event (the system works like that on discord)
async def on_message(message):

    message.content = message.content.upper()        # makes all the received message content upper
    if message.author.id == 682627598014218249:      # if the user id is equal to this one which is the bot id stops the whole message procces
        return

    if message.content.startswith("HOLA") or message.content.startswith("HI") or message.content.startswith("HELLO") or message.content.startswith("HELLU")  or message.content.startswith("HELLOW") or message.content.startswith("HEY") or message.content.startswith('HEL'):
        await message.channel.send(f"Hi {message.author.mention}")

    if message.content.find("!EXPLOSION") != -1:
        await message.channel.send(file=discord.File('tenor5.gif'))
        time.sleep(1)
        await message.channel.send(':star: Darkness blacker than black and darker than dark, I beseech thee, combine with my deep crimson :star:')
        time.sleep(2)
        await message.channel.send(':star: The time of awakening cometh. Justice, fallen upon the infallible boundary, appear now as an intangible distortion! Dance, Dance, Dance! :star:')
        time.sleep(2)
        await message.channel.send(':star: desire for my torrent of power a destructive force: a destructive force without equal! :star:')
        time.sleep(2)
        await message.channel.send(':star: Return all creation to cinders, and come from the abyss! :star:')
        time.sleep(2)
        await message.channel.send(':star: EXPLOSION!!!! :star:')
        await message.channel.send(file=discord.File('tenor.gif'))
        time.sleep(1)
        await message.channel.send(file=discord.File('tenor2.gif'))
        time.sleep(1)
        await message.channel.send(file=discord.File('tenor3.gif'))

    if message.content.startswith('?'):
        message.content = message.content.replace('?','')
        await message.channel.send(GoogleSearch(message.content))
        a = random.randint(0,3)
        if a == 0:
            await message.channel.send(file=discord.File('tenor4.gif'))
        elif a == 1:
            await message.channel.send(file=discord.File('tenor8.gif'))
        elif a == 2:
            await message.channel.send(file=discord.File('tenor9.gif'))
        elif a == 3:
            await message.channel.send(file=discord.File('tenor10.gif'))
        return
    if message.content.find('!JOIN') != -1:
        author = message.author
        await message.channel.send(join(author))

    if message.content.find():
        await message.channel.send()

    if message.content.find():
        await message.channel.send()

bot = commands.Bot(command_prefix="|")

async def join(author):

    channel = author.VoiceChannel
    await bot.VoiceChannel.connect(channel)

client.run(token)                          # connect code to the chat bot by using the token link(another holy prayer of discord)