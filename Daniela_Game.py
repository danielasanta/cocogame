#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 11 14:27:46 2018

@author: danielasantacruzaguilera
"""
"""
Introduction:
    This game is based on the movie Coco from Disney Pixar 2017, it also 
    includes other features from Mexican traditions and culture. 
    It consists of 4 stages, and 3 more defined functions to start playing
    win and game over.
    For those who haven't watched the movie, Day of the dead is a day to
    remember friends and family members who have died, and help support their 
    spiritual journey. On this day you place an "ofrenda" with traditional 
    Mexican food, drinks, flowers, canddles and the pictures of the beloved 
    people that are gone, so they can return for this day, enjoy it, and 
    later return to their peaceful resting.
    Coco trailer: https://www.youtube.com/watch?v=xlnPHQ3TLX8
    Day of the Dead: https://www.tripsavvy.com/day-of-the-dead-in-mexico-1588764
   
    Stage 1: Decide to go back to the living world or not.
    Stage 2: Get to the top of the Teotihuacan pyramid.
    Stage 2.1: (Dependent on Stage 2 decision) Fight the jaguar.
    Stage 3: Check point to cross to the living world.
    
Known Bugs and/or Errors:
    1)The inputs need an enter after the texr or it won't continue
    
"""

from sys import exit
import random

def play():
    print("Hello inmortal, what is your name?")
    name= input(">   \n")
    print(f""" 
Welcome to the dead world {name}, you don't remember what happened to you, 
do you? 
Here's a reminder: A week ago you were eating enchiladas and drinking tequila 
with your family, oh you're Mexican, just in case you didn't remember that either,
anyway, you had too much tequila and you died so now you're here. 
Would you like to return to the living world? 
    """)
    living_world()
    
def living_world():
    answer= input('Y/N:  ')
    if 'Y' in answer or 'y' in answer or 'yes' in answer or 'Yes' in answer or 'YES' in answer:
        print("""
Great, today is the day for that. Once a year all the dead can go back to the 
living world for just one day, to see their family and friends, eat delicious 
Mexican food and drink tequila, or in your case maybe not,just hot chocolate 
would do. In order to make it you have to pass some tests.
        """)
        input("Press enter to continue\n")
        pyramid()
        
    elif 'N' in answer or 'n' in answer or 'no' in answer or 'No' in answer or 'No' in answer:
        print(f"Oh well enjoy your stay in the dead world, maybe next year.")
        print("Would you like to play again?")
        play_again= input('Y/N: ')
        if 'Y' in play_again or 'y' in play_again or 'yes' in play_again or 'Yes' in play_again or 'YES' in play_again:
            play()
        elif 'N' in play_again or 'n' in play_again or 'no' in play_again or 'No' in play_again or 'NO' in play_again:
            exit()
        else:
            print("Sorry I didn't get that, leaving the game....")
            exit()
    else:
        print("Sorry I didn't get that, please choose Y or N")
        input("Press enter to continue\n")
        play()

def pyramid():
    print("""
The first test is getting to the top of the Teotihuacan pyramid, how would you 
like to get there?
    a)walk up (takes 7 hours) 
    b)fly up 
    c)stay down
    """)
    option= input(">   \n")
    
    if 'a' in option or 'A' in option or 'walk up' in option or 'walk' in option:
        print("""
Great, it'll take some time, but you'll go directly to the check point without
having to fight a jaguar, fiuu :D
        """)
        input("Press enter to go to the top of the pyramid\n")
        check_point()
        
    elif 'b' in option or 'B' in option or 'fly up' in option or 'fly' in option:
        print("""
Great option! This tells us you're a little bit lazy, and for that, you'll have
to fight a jaguar first.
        """)
        input("Press enter to continue\n")
        fight_jaguar()
        
    elif 'c' in option or 'C' in option or 'stay down' in option or 'stay' in option:
        print(f"Oh well enjoy your stay in the dead world, maybe next year.")
        input("Press enter to exit the game\n")
        exit()
    else:
        print("Sorry I didn't get that, please choose a, b or c")
        pyramid()
        
def fight_jaguar(): 
    print("""
Watch out for the Jaguar! He's approaching to you, what do you want to do?
    1) fight him
    2) jump and hope he won't get you
    """)
    decision = input(">   \n")
    if '1' in decision or 'fight' in decision or 'Fight' in decision:
        print("Punch the jaguar 6 times to beat him!")
        punches = 6
        while punches > 0 :
            print(punches)
            punches -= 1
            input("Press enter to punch!\n")
        print("""
Awww poor Jaguar, oh well, you get to fly to the top of the pyramid and
go to the check point!
        """)
        input("Press enter to fly to the top of the pyramid\n")
        check_point()
        
    elif '2' in decision or 'jump' in decision or 'Jump' in decision:
        print("""Oh no! The Jaguar jumps higher than you!  ¯\_ツ_/¯ 
        """)
        game_over()
        
    else:
        print("Sorry I didn't get that, please choose 1 or 2")
        input("Press enter to continue")
        fight_jaguar()

def check_point():
    print("""
You're finally at the top of the Teotihuacan pyramid, almost ready to enjoy
your time with family and friends, the last test is a check point, the
dead world police has to make sure you meet the requirements to pass to the 
living world for the day. To do so, answer the next question:
    """)
    questions = ['Did your family put up your photo in the ofrenda?',
                 'Will you drink hot chocolate or tequila?',
                 'What movie is this game based on?']
    quest = 1
    
    while quest > 0:
        quest_random = random.choice(questions)
        input("Press enter to continue\n")
        print(quest_random)
        print(" ")
        
        if quest_random == questions[0]:
            print("1) No\n2) Yes")
        
            answer1 = input("> \n")
            
            if answer1 == '2':
                print("Good! you can go on\n")
                quest -=1
            
            else: 
                print("""Sorry looks like your family already forgot about you,
                      try again next year.
                      """)
                game_over()
        
        elif quest_random == questions[1]:
            print("1) Hot Chocolate\n2) Tequila")
            
            answer2 = input("> \n")
            
            if answer2 == '1':
                print("Looks like you learnt the lesson, you can go on.\n")
                quest -=1
            
            else: 
                print("""Oh no, wrong answer, haven't you learnt the lesson?
                #facepalm
                """)
                game_over()

        elif quest_random == questions[2]:
            print("1) Coco\n2) Casper the friendly ghost")
            
            answer3 = input("> \n")
            
            if answer3 == '1':
                print("Good! Isn't it the sweetest movie?.\n")
                quest -=1
            
            else: 
                print("Sorry, wrong answer, watch the movie Coco please.\n")
                game_over()
            
                break
            
    print("You made it through the check point!\n")
    input("Press enter to continue\n")
    win()
    
def win():
    print("""
     _,-._
    / \_/ \    
    >-(_)-<    
    \_/ \_/
      `-'
    Welcome to the Living World enjoy your day!
    ********************************************                                          
        """)
    input("Press enter to exit, great job!\n")
    exit(0)
    
def game_over():
    print("""
 ██████╗  █████╗ ███╗   ███╗███████╗     ██████╗ ██╗   ██╗███████╗██████╗ 
██╔════╝ ██╔══██╗████╗ ████║██╔════╝    ██╔═══██╗██║   ██║██╔════╝██╔══██╗
██║  ███╗███████║██╔████╔██║█████╗      ██║   ██║██║   ██║█████╗  ██████╔╝
██║   ██║██╔══██║██║╚██╔╝██║██╔══╝      ██║   ██║╚██╗ ██╔╝██╔══╝  ██╔══██╗
╚██████╔╝██║  ██║██║ ╚═╝ ██║███████╗    ╚██████╔╝ ╚████╔╝ ███████╗██║  ██║
 ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝     ╚═════╝   ╚═══╝  ╚══════╝╚═╝  ╚═╝
    """)
    input("Press enter to exit\n")
    exit(0)
play()

    
        
    


    



