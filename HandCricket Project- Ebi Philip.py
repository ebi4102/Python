#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import random

def firstbating():
    global GameOver  
    print("Go for your first batting")
    runs = 0
    airuns = 0

    while not GameOver:  
        user = int(input("You may do batting:"))
        ai = random.randint(1, 6)
        print("AI bowling:", ai)
        runs += user
        print("Current runs of user is:", runs)

        if user == ai:
            print("User is out")
            print("AI's turn for batting")
            print("AI needs", (runs + 1), "to win the match")

            while True:
                user = int(input("You may do bowling:"))
                ai = random.randint(1, 6)
                print("AI batting:", ai)
                airuns += ai
                print("Current runs of AI is:", airuns)

                if airuns > runs:
                    print("AI won the match\nBetter luck next time")
                    GameOver = True 
                    break

                elif user == ai:
                    print("Successfully taking the wicket of AI")
                    print("You have won the match by", (runs - airuns), "runs")
                    GameOver = True  
                    break

def firstbowling():
    global GameOver  
    print("Go for your first bowling")
    runs = 0
    airuns = 0
    
    while not GameOver: 
        user = int(input("You may do bowling:"))
        ai = random.randint(1, 6)
        print("AI batting:", ai)
        airuns += ai
        print("Current runs of AI is:", airuns)

        if user == ai:
            print("AI is out")
            print("User's turn for batting")
            print("User needs", (airuns + 1), "to win the match")

            while True:
                user = int(input("You may do batting:"))
                ai = random.randint(1, 6)
                print("AI bowling:", ai)
                runs += user
                print("Current runs of user is:", runs)

                if runs > airuns:
                    print("User won the match")
                    GameOver = True  
                    break

                elif user == ai:
                    print("AI successfully taking the wicket of user")
                    print("AI have won the match by", (airuns - runs), "runs")
                    GameOver = True  
                    break

print("Welcome to HandCricket")
name = input("Please enter your name: ")
toss = input("Choose odd or even: ")
user = int(input("Choose a number between 1-6: "))

if user > 6 or user < 0:
    print("Invalid input")
else:
    ai = random.randint(1, 6)
    print("Input of AI:", ai)
    GameOver = False  
    if toss.lower() == "even":
        if (user + ai) % 2 == 0:
            print("You have won the toss\nchoose Bating or Bowling")
            tossinput = input("choose BAT or BALL:")
            if tossinput == "BAT":
                firstbating()
                
            elif tossinput == "BALL":
                firstbowling()
            else:
                print("Invalid input")
        else:
            print("AI has won the toss")
            aiinput = random.choice(["BAT", "BALL"])
            if aiinput == "BAT":
                print("ai is bating first")
                firstbowling()
            elif aiinput == "BALL":
                print("ai is bowling first")
                firstbating()
    elif toss.lower() == "odd":
        if (user + ai) % 2 != 0:
            print("You have won the toss\nchoose Bating or Bowling")

            tossinput = input("choose BAT or BALL:").upper()
            
            if tossinput == "BAT":
                firstbating()
            elif tossinput == "BALL":
                firstbowling()
            else:
                print("Invalid input")
        else:
            print("AI has won the toss")
        aiinput = random.choice(["BAT", "BALL"])
        if aiinput == "BAT":
            print("ai is bating first")
            firstbowling()
            
        elif aiinput == "BALL":
            print("ai is bowling first")
            firstbating()

