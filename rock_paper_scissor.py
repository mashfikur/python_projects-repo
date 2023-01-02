import random

user_score=0
system_score=0

options=["rock","paper","scissor"]

while True:
    user_move=input("Type rock/paper/scissor or q to quit :").lower()

    if user_move=="q":
        break
    
    if user_move not in options :
        print("Type your move")
        continue

    random_pick=random.randint(0,2)

    system_move=options[random_pick]
    print("computer picked",system_move)


    if user_move=="rock" and system_move=="scissor":
        print("You won!")
        user_score+=1
    
    elif user_move=="paper" and system_move=="rock":
        print("You won!")
        user_score+=1
    
    elif user_move=="scissor" and system_move=="paper":
        print("You Won!")
        user_score+=1
    else:
        print("You lost")
        system_score+=1
        

print("You won",user_score,"times .")
print("System won",system_score,"times .")
    

    

    

