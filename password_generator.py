import random
import string
print("welcome to password generator")
length=int(input("enter the length of password:"))
user_upper=input("do you want uppercase(y/n)")
user_numbers=input("do you want numbers(y/n)")
user_symbols=input("do you want symbols(y/n)")

character=string.ascii_lowercase

if user_upper=="yes":
    character=string.ascii_uppercase

if user_numbers=="yes":
    charecter=string.digits
if user_symbols=="yes":
    chacter=string.punctuation

password=""

for i in range(length):
    password+=random.choice(character)

print("generated password:",password)