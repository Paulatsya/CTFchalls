from pwn import *
import string


def count_vowels(s):
    return sum(1 for c in s.lower() if c in "aeiou")


io = remote('localhost', 54318)

for i in range(10):
    io.recvline()
    prompt = io.recvline_contains(b"Count the vowels in this string:")
    try:
        challenge_str = prompt.split(b":", 1)[1].strip().decode()
    except Exception as e:
        print("Error parsing challenge string:", e)
        exit()

    answer = count_vowels(challenge_str)
    # Send the answer
    io.sendline(str(answer).encode())

io.interactive()
