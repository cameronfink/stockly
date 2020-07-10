from random import randint, seed
import string
import random
import keyboard
from time import sleep
from os import system, name

seed(randint(0,1000))

# Clear screen function
def clear(): 
    if name == 'nt': 
        _ = system('cls') 
    else: 
        _ = system('clear') 

# Opening and closing screen
def openingScreen():
    print('Welcome to the Stockly proof of concept.')
    print('This is version 0.0.1 Stellenbosch.')
    print('Copyright Cameron Fink 2020')

def closingScreen():
    print('\nThank you for using Stockly.')
    print('Contact Cameron Fink for any questions, comments or concerns.')

# Setting variables
watchList = ''

# Defining 30 basic stocks
stock1 = 'MSFT | Microsoft | Consumer Electronics'
stock2 = 'AAPL | Apple | Consumer Electronics'
stock3 = 'AMZN | Amazon | Ecommerce'
stock4 = 'GOOGL | Alphabet | Consumer Electronics'
stock5 = 'BABA | Alibaba | Ecommerce'
stock6 = 'FB | Facebook | Consumer Services'
stock7 = 'BRK.B | Berkshire Hathaway | Financial Services'
stock8 = 'V | Visa | Financial Services'
stock9 = 'AMD | Advanced Micro Devices | Electronics'
stock10 = 'JNJ | Johnson & Johnson | Consumer Cyclicals'
stock11 = 'GS | Goldman Sachs | Financial Services'
stock12 = 'XOM | Exxon Mobile | Energy'
stock13 = 'SPCE | Virgin Galactic | Aerospace & Defence'
stock14 = 'ROKU | Roku | Consumer Electronics'
stock15 = 'WBA | Walgreens Boots Alliance | Retail'
stock16 = 'MRNA | Moderna | Biotech'
stock17 = 'NVAX | Novavax | Biotech'
stock18 = 'LVGO | Livongo | Biotech'
stock19 = 'CSCO | Cisco | Consumer Electronics'
stock20 = 'UAL | United Airlines | Aerospace & Defence'
stock21 = 'CCL | Carnival | Consumer Discretionary'
stock22 = 'AAL | American Airlines | Aerospace & Defence'
stock23 = 'LMT | Lockheed Martin | Aerospace & Defence'
stock24 = 'NOC | Northrop Grumman | Aerospace & Defence'
stock25 = 'I | Intelsat | Aerospace & Defence'
stock26 = 'BA | Boeing | Aerospace & Defence'
stock27 = 'RTX | Raytheon Technologies | Aerospace & Defence'
stock28 = 'MAXR | Maxr Technologies | Aerospace & Defence'
stock29 = 'TXT | Textron | Aerospace & Defence'
stock30 = 'TXN | Texas Instruments | Electronic Components'

stockList = []

for i in range(30):
  stockList.append(vars()['stock' + str(i+1)])

# Random Stock
def stockMatch():
    global watchList
    stockChoice = random.choice(stockList)
    stockIndex = stockList.index(stockChoice)
    del stockList[int(stockIndex)]
    print(stockChoice)
    moveInput = input('Swipe left or right. ')
    if moveInput == 'l':
        watchList = stockChoice + ', ' + watchList

def viewList():
    global watchList
    viewlistInput = input('Do you wish to view your list? y/n ')
    if viewlistInput == 'y':
        print(str(watchList))
    elif viewlistInput == 'n':
        print('You have selected not to view your watchlist.')

# Cycle of 10 stocks
openingScreen()
sleep(3)

for i in range(20):
    clear()
    stockMatch()
    viewList()
    sleep(3)

closingScreen()
sleep(10)
clear
