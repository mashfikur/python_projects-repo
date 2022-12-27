import random

start_range=input("Type a number limit :")

if start_range.isdigit():
    start_range=int(start_range)

    if start_range<=0:
        print("Type a number larger than 0")
        quit()
else:
    print("Please type a number")
    quit()

random_number=random.randint(1,start_range)

guess=0

while True:
    guess+=1
    user_guess=input("Guess a number :")

    if user_guess.isdigit():
        user_guess=int(user_guess)

    else:
        print("Guess a actual number")
        continue
    
    if user_guess==random_number:
        print("You got it right!")
        break
    elif user_guess>random_number:
        print("You are larger than the number")
    else:
        print("You are less than the number")

        

print("Your total guess is :",guess)







