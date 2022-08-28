import random
print(""" 
 ██████╗ ██╗   ██╗███████╗███████╗███████╗    ███╗   ██╗██╗   ██╗███╗   ███╗██████╗ ███████╗██████╗ 
██╔════╝ ██║   ██║██╔════╝██╔════╝██╔════╝    ████╗  ██║██║   ██║████╗ ████║██╔══██╗██╔════╝██╔══██╗
██║  ███╗██║   ██║█████╗  ███████╗███████╗    ██╔██╗ ██║██║   ██║██╔████╔██║██████╔╝█████╗  ██████╔╝
██║   ██║██║   ██║██╔══╝  ╚════██║╚════██║    ██║╚██╗██║██║   ██║██║╚██╔╝██║██╔══██╗██╔══╝  ██╔══██╗
╚██████╔╝╚██████╔╝███████╗███████║███████║    ██║ ╚████║╚██████╔╝██║ ╚═╝ ██║██████╔╝███████╗██║  ██║
 ╚═════╝  ╚═════╝ ╚══════╝╚══════╝╚══════╝    ╚═╝  ╚═══╝ ╚═════╝ ╚═╝     ╚═╝╚═════╝ ╚══════╝╚═╝  ╚═╝
                                                                                                    
""")
print("Welcome to Guessing number game ")
level = input("Select level: 'easy' or 'hard' : ").lower()

number = random.randint(1,100)

def is_number(player_guess):
    global number
    if player_guess < number:
        if number - player_guess >10:
            return "Too low"
        else:
            return "Low"
    elif player_guess> number:
        if player_guess-number>10:
            return "Too high"
        else:
            return "High"
    else:
        return 0


if level == "easy":
    attempt = 10
else:
    attempt = 5

print(f"You have {attempt} attempts.")   
num_is_guessed = False
guess_num = int(input("Guess a number from 1 to 100 : "))
while not num_is_guessed:
   
    check = is_number(guess_num)
    if  check == 0:
        print(f"You have guessed the number, the number is {number}")
        num_is_guessed = True
        
    else:
        print(check)
        attempt-=1
        if attempt == 0:
            print("You have no attepts left")
            print("Game over, You lose")
            print(f"The number is {number}")
        print(f"You have {attempt} attempts left")
        guess_num = int(input("Guess again:  "))
