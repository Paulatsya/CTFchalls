import socket
import random
import time

# Function to count the occurrences of a specific digit in a range
def count_digit_in_range(start, end, digit='2'):
    count = 0
    for number in range(start, end + 1):
        count += str(number).count(digit)
    return count

# Function to generate a random question
def generate_question():
    start = random.randint(1, 1000)
    end = random.randint(start + 1, 2000)
    return start, end

def start_server():
    # Set up the server to listen on a specified port
    host = '0.0.0.0'  # Listen on all available interfaces
    port = 12345        # Choose an arbitrary port (make sure it's open)

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))
    server.listen(1)
    print(f"Server listening on {host}:{port}...")

    while True:
        # Accept a connection from a client
        client_socket, addr = server.accept()
        print(f"Connection from {addr}")

        # Send a welcome message
        client_socket.send(b"Welcome to the CTF challenge! Solve 10 questions in under 10 seconds each.\n")

        correct_answers = 0
        total_time = 0
        question_limit = 10
        question_start_time = time.time()

        # Start the challenge loop
        try:
            while correct_answers < question_limit:
                # Generate a random question
                start, end = generate_question()
                question = f"How many times does the digit 2 appear between {start} and {end}?\n"
                client_socket.send(question.encode())

                # Record the start time for the question
                start_time = time.time()

                # Wait for the answer from the client
                client_socket.settimeout(10)  # 10 seconds to answer
                answer = client_socket.recv(1024).decode().strip()

                # Calculate the time taken for the answer
                answer_time = time.time() - start_time

                if answer.lower() == 'exit':
                    client_socket.send(b"Goodbye!\n")
                    break

                if answer_time > 10:
                    client_socket.send(b"Time's up! You took too long to respond.\n")
                    continue  # Skip this question and move to the next one

                try:
                    # Check if the answer is correct
                    correct_answer = str(count_digit_in_range(start, end, '2'))
                    if answer == correct_answer:
                        correct_answers += 1
                        total_time += answer_time
                        client_socket.send(f"Correct! You have answered {correct_answers} out of {question_limit} questions.\n".encode())
                    else:
                        client_socket.send(f"Incorrect. The correct answer was {correct_answer}. You have answered {correct_answers} questions correctly.\n".encode())
                except ValueError:
                    client_socket.send(b"Invalid answer. Please send a number.\n")
        
            if correct_answers == question_limit:
                client_socket.send(b"Congratulations! You've solved 10 questions under 10 seconds each!\n")

        except socket.timeout:
            client_socket.send(b"Time's up! You took too long to respond.\n")
        except Exception as e:
            print(f"Error: {e}")
        
        # Close the client connection
        client_socket.close()

if __name__ == "__main__":
    start_server()
