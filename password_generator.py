import random,string
password=""
l=int(input("Enter password length: "))
c=string.ascii_letters+string.digits+string.punctuation
for i in range(l):
    password+=random.choice(c)
print("Password you can use :",password)