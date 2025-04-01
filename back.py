import random

number_to_guess = random.randint(1,100)
attempts = 5

while attempts > 0:
    try:
        guess = int(input("ENTER A GUESS OF THE NUMBER BETWEEN 1-100: "))
        if guess < 1 or guess > 100:
            print('invalid guess')
            continue
        if guess == number_to_guess:
            print("Your guess was right ")
        elif guess > number_to_guess:
            print("YOUR GUESS IS TO HIGH")
        elif guess < number_to_guess:
            print("YOUR GUESS IS TO LOW")
            
        attempts -= 1
        
    except ValueError:
        print("Enter a valid guess")
    
if attempts == 0:
    print(f"you are out attempts the number to guess was:{number_to_guess}")