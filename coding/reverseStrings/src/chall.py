import random
import time

starting_time = int(time.time())  

def generate_string(length=8):
    return ''.join(random.choices('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ', k=length))

def start_challenge():
    correct_answers = 0
    question_limit = 10

    for i in range(1, question_limit + 1):
        print(f'Round {i}!')
        random_string = generate_string()
        current_time = int(time.time())
        if current_time - starting_time > 60:
            print("Time's up! You've exceeded the time limit.")
            exit()
        user_answer = input(f"Please reverse this string: {random_string}\n")
        
        if user_answer == random_string[::-1]:
            print("Correct! Moving on to the next round.")
            correct_answers += 1
        else:
            print(f"Incorrect!")
            print("Game over!")
            exit()

        if i == question_limit:
            with open('flag.txt', 'r') as f:
                print(f.read())
            break

if __name__ == "__main__":
    start_challenge()
