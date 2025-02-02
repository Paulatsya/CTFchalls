from pwn import *

# io = process('../src/chall.py')
io = remote('localhost', 54321)

def solve(x, start, end):
    # Count the occurrences of the digit 'x' between start and end
    answer = 0
    for i in range(start, end + 1):
        answer += str(i).count(x)
    return answer

for i in range(1, 11):  # Loop over 100 rounds
    if i > 1:
        io.readline()  # Skip the previous round output
    io.readline()  # Read the "Round X!" line
    io.readuntil(b'How many ')  # Read up to the question

    line = io.readline().strip()  # Read the question
    print(f"Line: {line}")  # Debug the line content

    x = chr(int(line[0]))  # Extract the digit we are counting (we assume it is the first character)
    
    # Extract the start and end from the question
    # We'll use regex to extract the two numbers from the question
    import re
    match = re.search(r'between (\d+) and (\d+)', line.decode())  # Find numbers between 'between' and 'and'
    if match:
        start, end = map(int, match.groups())
        print(f"Start: {start}, End: {end}")  # Debug the extracted start and end
    else:
        print("Failed to extract range")
        continue  # Skip this round if parsing fails

    # Calculate the correct answer
    answer = solve(x, start, end)

    # Send the answer back to the server
    io.sendline(str(answer).encode())

# Print the interactive output after the challenge is complete
io.interactive()
