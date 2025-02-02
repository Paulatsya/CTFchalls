from pwn import *

# io = process('../src/chall.py')
io = remote('localhost', 54321)

for i in range(1, 11):  # Loop over 100 rounds
    if i > 1:
        io.readline()  # Skip the previous round output
    io.readline()  # Read the "Round X!" line
    io.readuntil(b'Please reverse this string: ')  # Read up to the string question

    line = io.readline().strip()  # Read the string to be reversed
    print(f"String to reverse: {line}")  # Debug: print the string to reverse

    # Reverse the string
    reversed_string = line[::-1]
    print(f"Reversed string: {reversed_string}")  # Debug: print the reversed string

    # Send the reversed string back to the server
    io.sendline(reversed_string)

# Print the interactive output after the challenge is complete
io.interactive()
