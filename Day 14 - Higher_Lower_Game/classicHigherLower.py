# Classic Higher-Lower game - Instagram followers version
import random
from art import logo, vs
from game_data import data
from replit import clear

def format_account_data(account):
    account_name = account["name"]
    account_description = account["description"]
    account_country = account["country"]
    
    return f"{account_name}, a {account_description}, from {account_country}"

def check_answer(guess, A_followers, B_followers):
    if A_followers > B_followers:
        return guess == 'a'
    else:
        return guess == 'b'

def higher_lower():
    print(logo)
    show_must_go_on = True
    score = 0
    # first_account = random.choice(data)
    second_account = random.choice(data)
    
    while show_must_go_on:
        first_account = second_account
        second_account = random.choice(data)
        
        while first_account == second_account:
            second_account = random.choice(data)
            
        print(f"Compare A: {format_account_data(first_account)}.")
        print(vs)
        print(f"Compare B: {format_account_data(second_account)}.")

        answer = input('Who has more followers? Type A or type B: ').lower()
        followers_A = first_account["follower_count"]
        followers_B = second_account["follower_count"]

        is_correct = check_answer(answer, followers_A, followers_B)

        clear()
        print(logo)
        if is_correct:
            score += 1
            print(f"You're right! Your score: {score}.")
        else:
            show_must_go_on = False
            print(f"Hah, that's wrong. Final score: {score}")
            print(f"{first_account['name']} - {followers_A}M followers")
            print(f"{second_account['name']} - {followers_B}M followers")
            print('Cannot you go up to 10? hah...')    
higher_lower()