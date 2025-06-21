import random

print("welcome to number guessing game")
while True:
    try:
        start=int(input("Enter the start number: "))
        end=int(input("Enter the end number: "))
        break
    except ValueError:
        print("please enter a numbers only")


difficulty = input("Choose difficulty (easy/medium/hard): ")
if difficulty == "easy":
    tries=5
elif difficulty == "hard":
    tries=2
else: #this will be the default also
    tries=3



number = random.randint(start, end)
left=tries
print(f"i picked a number between {start} and {end} u have {tries} tries. ")

while left !=0:

    while True:
        try:
            c = int(input("enter ur guess: "))
            break
        except ValueError:
            print("please guess a number only")

    left = left - 1
    if c==number:
        print(f"Correct! The number was {number}.")
        break
    else:
        print(f"wrong guess. {left} attempts left")
   