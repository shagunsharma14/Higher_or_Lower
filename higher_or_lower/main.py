from game_data import data
import random
from art import logo, vs
import os

def random_account():
    return random.choice(data)


def format_data(account):
    name = account["name"]
    description = account["description"]
    country = account["country"]
    return f"{name},a {description} from {country}"


def check_answer(guess, follower_count_a, follower_count_b):
    if follower_count_a > follower_count_b:
      return guess == "a"  #returning true if guess is correct
    else:
      return guess == "b"  #returning true if guess is correct


def game():
  print(logo)
  score = 0
  game_countinue=True
  account_a = random_account()
  account_b = random_account()
  while game_countinue:
    account_a=account_b
    account_b=random_account()
    while account_a==account_b:
      account_b=random_account()
        
    print(f"Compare A: {format_data(account_a)}")
    print(vs)
    print(f"Compare B: {format_data(account_b)}")

    guess = input("Who has the more followers, Type 'a' or 'b': ").lower()
    follower_count_a = account_a["follower_count"]
    follower_count_b = account_b["follower_count"]
    is_correct = check_answer(guess, follower_count_a, follower_count_b)
    os.system('cls')
    print(logo)

    if is_correct:
      score += 1
      print(f"You're right: current score{score}")
    else:
      game_countinue=False
      print(f"You're wrong: your score is {score}")
game()
