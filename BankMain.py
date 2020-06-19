# BankMain.py
import Login
import Menu
import Balance
import Transactions
import pygame
from pygame import mixer

# pygame.mixer.init()
# pygame.mixer.music.load("TheSea.mp3")
# pygame.mixer.music.play()

print("welcome")

if(Login.performLogin() == True):
    Menu.displayMenu()
    # Balance.displayBalance(accountNumber=0)
else:
    print("Please try again.")
    print("You have one try left.")
    if (Login.performLogin() == True):
        Menu.displayMenu()


