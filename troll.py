
import time
import os
import sys


#to hide - welcome to pigame message
#source: Stackoverflow users Wombatz and Coder Gautam YT
from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
    

import pygame




# introduce mixer that will allow us to play song
pygame.mixer.init()



#stimulates something is actually scanning ...
print("Now generating packets ...")
time.sleep(1)
print("Scanning packets 01/34: Progress: 1% ")
time.sleep(1)
print("Scanning packets 02/34: Progress: 3% ")
print("Scanning packets 03/34: Progress: 7% ")
time.sleep(1)
print("Scanning packets 04/34: Progress: 10% ")
time.sleep(3)
print("Scanning packets 05/34: Progress: 12% ")
time.sleep(3)
print("Scanning packets 06/34: Progress: 15% ")
time.sleep(1)
print("Scanning packets 07/34: Progress: 20% ")
time.sleep(1)
print("Scanning packets 08/34: Progress: 22% ")
time.sleep(1)
print("Scanning packets 09/34: Progress: 25% ")
time.sleep(1)
print("Scanning packets 10/34: Progress: 27% ")
time.sleep(1)
print("Scanning packets 11/34: Progress: 29% ")
time.sleep(2)
print("Scanning packets 12/34: Progress: 30% ")
time.sleep(5)
print("Scanning packets 13/34: Progress: 35% ")
time.sleep(1)
print("Scanning packets 14/34: Progress: 38% ")
time.sleep(1)
print("Scanning packets 15/34: Progress: 40% ")
time.sleep(1)
print("Scanning packets 16/34: Progress: 43% ")
time.sleep(1)
print("Scanning packets 17/34: Progress: 45% ")
time.sleep(1)
print("Scanning packets 18/34: Progress: 48% ")
time.sleep(1)
print("Scanning packets 19/34: Progress: 50% ")
time.sleep(5)
print("Scanning packets 22/34: Progress: 54% ")
time.sleep(5)
print("Scanning packets 24/34: Progress: 65% ")
time.sleep(10)
print("Scanning packets 27/34: Progress: 72% ")
time.sleep(10)
print("Scanning packets 31/34: Progress: 85% ")
time.sleep(10)
print("Scanning packets 33/34: Progress: 90% ")
time.sleep(5)
print("Scanning packets 33/34: Progress: 99% ")
time.sleep(10)
print("Scanning packets 34/34: Progress: 100% ")
time.sleep(5)

print("\n")
print("Packets loaded ...")

#prints fake set of usernames and passwords
with open('UserPassword.txt', 'r') as file:
    lines = file.readlines()
# Print fake packets
for line in lines:
    print(line.strip())



#REMINDER: FBI alarm plays !!!!!!!!!!!!!!!!!!!!!!!!
pygame.mixer.music.load("fbi_siren.mp3")
pygame.mixer.music.play(5)
time.sleep(1)
print("\n" + "-"*50 + "\n")
print("HACKER DETECTED! HACKER DETECTED! HACKER DETECTED!")
print("-"*50 + "\n")
time.sleep(3)


#REMINDER: Rick Roll Music !!!!!!!!!!!!!!!!!!!!!
pygame.mixer.music.load("rickroll.mp3")
pygame.mixer.music.play(5)  # Loop the song
time.sleep(2)
print("You are getting this message because you are trying to access a system that you are not authorized to acess")
print("Because you have chosen to steal user information, here is a little song for you to think about your actions")
print("All of your actions in this system are monitored and logged including keystrokes")
print("-"*50 + "\n")



time.sleep(10)
print("COME ON,SING WITH ME!")

#another annoying message >> this will provide the lyrics to Baby Shark in a loop
#def display_annoying_message():
    

#play Baby shark here 
def song():
    pygame.mixer.music.load("annoyingMusic.mp3")
    pygame.mixer.music.play(-1)  # Loop the song

    
# Loop the song forever with no end 
song()


def foreverBabyShark():
    key = True
    while (key == True):
        print("baby shark, doo-doo, doo-doo, doo-doo baby shark, doo-doo, doo-doo, doo-doo baby shark, doo-doo, doo-doo, doo-doo baby shark")
        print("bAbY ShArK, dOo-dOo, DoO-DoO, dOo-dOo bAbY ShArK, dOo-dOo, DoO-DoO, dOo-dOo bAbY ShArK, dOo-dOo, DoO-DoO, dOo-dOo bAbY ShArK")
        print("BABY SHARK, DOO-DOO, DOO-DOO, DOO-DOO BABY SHARK, DOO-DOO, DOO-DOO, DOO-DOO BABY SHARK, DOO-DOO, DOO-DOO, DOO-DOO BABY SHARK")
        print("baby shark, doo-doo, doo-doo, doo-doo baby shark, doo-doo, doo-doo, doo-doo baby shark, doo-doo, doo-doo, doo-doo baby shark")
        print("bAbY ShArK, dOo-dOo, DoO-DoO, dOo-dOo bAbY ShArK, dOo-dOo, DoO-DoO, dOo-dOo bAbY ShArK, dOo-dOo, DoO-DoO, dOo-dOo bAbY ShArK")
        print("BABY SHARK, DOO-DOO, DOO-DOO, DOO-DOO BABY SHARK, DOO-DOO, DOO-DOO, DOO-DOO BABY SHARK, DOO-DOO, DOO-DOO, DOO-DOO BABY SHARK")
        print("baby shark, doo-doo, doo-doo, doo-doo baby shark, doo-doo, doo-doo, doo-doo baby shark, doo-doo, doo-doo, doo-doo baby shark")
        print("bAbY ShArK, dOo-dOo, DoO-DoO, dOo-dOo bAbY ShArK, dOo-dOo, DoO-DoO, dOo-dOo bAbY ShArK, dOo-dOo, DoO-DoO, dOo-dOo bAbY ShArK")
        print("BABY SHARK, DOO-DOO, DOO-DOO, DOO-DOO BABY SHARK, DOO-DOO, DOO-DOO, DOO-DOO BABY SHARK, DOO-DOO, DOO-DOO, DOO-DOO BABY SHARK")
        
        print("I hope you like Baby Shark, which will only keep repeating for the worst - unless you enter the secret key to stop")
        command = input("Enter the special password to stop: ")
        
        if (command.lower() == 'mommy shark' or command.lower() == 'Mommy shark' or command.lower() == 'MOMMY SHARK' or command.lower() == 'mOmMy ShArK'):
            print("Congrats! YOU CRACKED THE CODE!!!")
            print("goodbye hacker, we hope you learned your lesson :)")
            pygame.mixer.music.stop() #stops song
            break
        else:
            pygame.mixer.music.play(0)  # restart the song
            print("Incorrect Message - Please Try Again")

            
foreverBabyShark()











