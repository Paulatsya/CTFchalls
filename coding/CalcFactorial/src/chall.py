#!/usr/bin/env python3
import random
import time
import math

starting_time = int(time.time())

def generate_number():
    return random.randint(0, 20)

def start_challenge():
    correct_answers = 0
    question_limit = 10

    for i in range(1, question_limit + 1):
        print(f'Round {i}!')
        number = generate_number()
        current_time = int(time.time())
        if current_time - starting_time > 60:
            print("Time's up! Exceeded 60 seconds.")
            exit()
        user_answer = input(f"Calculate the factorial of: {number}\n")
        
        try:
            if int(user_answer.strip()) == math.factorial(number):
                print("Correct! Moving on to the next round.")
                correct_answers += 1
            else:
                print("Incorrect!\nGame over!")
                exit()
        except ValueError:
            print("Invalid input!")
            exit()

        if correct_answers == question_limit:
            with open('flag.txt', 'r') as f:
                print(f.read())
            exit()

if __name__ == "__main__":
    start_challenge()