import random
#from replit import clear
from art import logo,vs
from game_data import data
def compare(followers_a,followers_b):
    if followers_a > followers_b:
        return "a"
    else:
        return "b"

def choose_person():
    person = data[random.randint(0,len(data)-1)]
    return person

print(logo)
print("Welcome to Higher Lower ")
correct = True

person_a = choose_person()
name_a = person_a["name"]
description_a = person_a["description"]
follower_a = person_a["follower_count"]
country_a= person_a["country"]
print(f"Compare A: {name_a}, a {description_a} from {country_a}")

print(vs)

person_b = choose_person()
name_b = person_b["name"]
description_b = person_b["description"]
follower_b = person_b["follower_count"]
country_b= person_b["country"]
print(f"Against B: {name_b}, a {description_b} from {country_b}")

your_guess = input("Who has more followers? Type 'A' or 'B': ").lower()
ans = compare(follower_a,follower_b)

current_score = 0
while correct:
    if your_guess == ans:
        #clear
        person_a = person_b
        name_a = person_a["name"]
        description_a = person_a["description"]
        follower_a = person_a["follower_count"]
        country_a= person_a["country"]

        person_b = choose_person()
        name_b = person_b["name"]
        description_b = person_b["description"]
        follower_b = person_b["follower_count"]
        country_b= person_b["country"]
        current_score +=1
        print(f"Your current score: {current_score}")
        print(f"Compare A: {name_a}, a {description_a} from {country_a}")
        print(vs)
        print(f"Against B: {name_b}, a {description_b} from {country_b}")
        your_guess = input("Who has more followers? Type 'A' or 'B': ").lower()
        ans = compare(follower_a,follower_b)
    else:
        print(f"You got Wrong, your score is {current_score}")
        correct = False