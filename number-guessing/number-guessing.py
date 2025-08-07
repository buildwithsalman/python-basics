import random 

target = random.randint(1,100)

guess = None
attempts = 0

while target != guess:
    guess = int(input("Guess a number between 1 , 100: "))
    attempts += 1
    if guess < target:
        print("too low")
    elif guess > target:
        print("to high")
    else:
        print(f"congrats!!, you have guessed it correct in just {attempts} attempts")


