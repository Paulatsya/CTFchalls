#!/usr/bin/env python3
import random
import time

starting_time = int(time.time())

def solve(start, end, digit='2'):
    count = 0
    for number in range(start, end + 1):
        count += str(number).count(digit)
    return count

def generate_question():
    start = random.randint(1, 1000)
    end = random.randint(start + 1, 2000)
    return start, end

def start_challenge():
    correct_answers = 0
    question_limit = 10

    for i in range(1, question_limit + 1):
        print(f'Round {i}!')
        start, end = generate_question()
        x = 2  # Fixed digit 2 for the challenge
        current_time = int(time.time())

        # Check if time limit exceeded
        if current_time - starting_time > 60:
            print("Time's up! You've exceeded the time limit.")
            exit()

        # Ask the user the question
        user_answer = input(f"How many {x}'s appear between {start} and {end}?\n")
        
        try:
            user_answer = int(user_answer.strip())
        except ValueError:
            print("Invalid input! Please enter a number.")
            continue

        # Calculate the correct answer
        correct_answer = solve(start, end, str(x))

        if user_answer == correct_answer:
            print("Correct! Moving on to the next round.")
            correct_answers += 1
    
        else:
            print(f"Incorrect! The correct answer was {correct_answer}.")
            print("Game over!")
            exit()

        if i == question_limit:
            print(open('flag.txt').read())
            break

if __name__ == "__main__":
    start_challenge()
