import random

number = random.randint(1,100)

print("############## Lets Play a Number Guessing Game #############")

count = 0
guessed = 0

while guessed!=number:
    guessed = int(input("Guess the number: "))

    if guessed < 1 or guessed > 100:
        print("Enter number between 1 to 100")
        continue
        
    count+=1
    
    if guessed >= number+10:
        print("Too High, Try Again")
    elif guessed <= number-10:
        print("Too low, Try Again")
    elif guessed == number:
        print(f"Correct Number!!!\nAttempted {count} times.")
        break
    
