#!/usr/bin/env python3
import random
import time
import string

# Define function to count vowels in a string
def count_vowels(s):
    return sum(1 for c in s.lower() if c in "aeiou")

# Generate a random string of letters of random length between 5 and 15
def generate_random_string():
    length = random.randint(5, 15)
    return ''.join(random.choice(string.ascii_letters) for _ in range(length))

def start_challenge():
    correct_answers = 0
    question_limit = 10
    starting_time = int(time.time())
    
    for i in range(1, question_limit + 1):
        print(f"Round {i}!")
        challenge_string = generate_random_string()
        current_time = int(time.time())
        # 30 second time limit for the entire challenge
        if current_time - starting_time > 30:
            print("Time's up! Exceeded 30 seconds.")
            exit()
        
        user_answer = input(f"Count the vowels in this string: {challenge_string}\n")
        
        try:
            if int(user_answer.strip()) == count_vowels(challenge_string):
                print("Correct! Moving on to the next round.")
                correct_answers += 1
            else:
                print("Incorrect!\nGame over!")
                exit()
        except ValueError:
            print("Invalid input!")
            exit()

    if correct_answers == question_limit:
        with open("flag.txt", "r") as f:
            print(f.read())
        exit()

if __name__ == "__main__":
    start_challenge()
