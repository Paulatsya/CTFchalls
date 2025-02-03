from pwn import *
import math

io = remote('localhost', 54319)  

for i in range(10):  # 10 rounds
    io.readline()  
    io.readuntil(b'Calculate the factorial of: ')
    num = int(io.readline().strip())
    fact = math.factorial(num)
    io.sendline(str(fact).encode())

io.interactive()  