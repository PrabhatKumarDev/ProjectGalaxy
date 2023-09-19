#Import the random module and os module
import random
import os
#Import logo from art.py
from art import logo,vs
#Import data list from data.py
from data import data

# Choose random candidate from data 
def choose_radom_candidata(candidate):
    random_number=random.randint(0,49)
    candidate=f"{data[random_number]['name']}, a {data[random_number]['description']}, from {data[random_number]['country']}."
    return candidate,data[random_number]['follower_count']

# Chekcs which candidate have more followeres
def check_who_has_more_followers(followers_1,followers_2):
    if(followers_1 > followers_2):
        return "a"
    elif(followers_1 < followers_2):
        return "b"
    else:
        return "Draw"

score=0
game_not_over=True
while(game_not_over):
    candidate_1= ""
    candidate_2=""
    candidate_1 = choose_radom_candidata(candidate_1)
    candidate_2 = choose_radom_candidata(candidate_2)
    print(logo)
    if(score>0):
        print(f"You're right! Current Score: {score}")

    print(f"Compare A: {candidate_1[0]}")

    print(vs)

    print(f"Against B: {candidate_2[0]}")

    user_answer=input("Who has more followers? Type 'A' or 'B': ")
    user_answer.lower()
    actual_answer=check_who_has_more_followers(candidate_1[1],candidate_2[1])
    if(user_answer==actual_answer):
        score+=1
        print(score)
        os.system('cls')
    
    else:
        os.system('cls')
        print(logo)
        print(f"Sorry, that's wrong. Final score: {score}")
        game_not_over=False




