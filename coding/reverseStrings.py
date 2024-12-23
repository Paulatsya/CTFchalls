import socket
import random
import string
import time

# Function to generate a random string
def generate_random_string(length=8):
    return ''.join(random.choices(string.ascii_lowercase + string.ascii_uppercase + string.digits, k=length))

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
        client_socket.send(b"Welcome to the String Reversal Challenge! Reverse 10 strings in under 10 seconds each.\n")

        correct_answers = 0
        question_limit = 10

        # Start the challenge loop
        try:
            while correct_answers < question_limit:
                # Generate a random string
                random_string = generate_random_string()
                question = f"Reverse this string: {random_string}\n"
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

                # Check if the answer is correct
                correct_answer = random_string[::-1]  # Reverse the string to get the correct answer
                if answer == correct_answer:
                    correct_answers += 1
                    client_socket.send(f"Correct! You have answered {correct_answers} out of {question_limit} questions.\n".encode())
                else:
                    client_socket.send(f"Incorrect. The correct answer was {correct_answer}. You have answered {correct_answers} questions correctly.\n".encode())

            if correct_answers == question_limit:
                client_socket.send(b"Congratulations! You've solved 10 string reversal questions under 10 seconds each!\n")

        except socket.timeout:
            client_socket.send(b"Time's up! You took too long to respond.\n")
        except Exception as e:
            print(f"Error: {e}")
        
        # Close the client connection
        client_socket.close()

if __name__ == "__main__":
    start_server()
