print("Welcome to my memory Quiz !")

player_will=input("Do you want to play ? Let us Know :")

score=0


if player_will.lower()=="yes":
    print("thank you,let's play")
else:
    quit()

q1=input("What is the full form of GPU? Ans:")

if q1=="Graphics Processing Unit":
    print("correct!")
    score+=1
else:
    print("wrong answer!")


q2=input("Who is the inventor of c programming? Ans:")

if q2=="Dennis Ritchie":
    print("correct!")
    score+=1
else:
    print("wrong answer!")


q3=input("What is spotify? Ans:")

if q3=="music streaming platform":
    print("correct!")
    score+=1
else:
    print("wrong answer!")


q4=input("Who is the rock? Ans:")

if q4=="a wrestler":
    print("correct!")
    score+=1
else:
    print("wrong answer!")


q5=input("Who invented facebook? Ans:")

if q5=="mark zukerberg":
    print("correct!")
    score+=1
else:
    print("wrong answer!")

q6=input("Who is the owner of Microsoft? Ans:")

if q6=="bill gates":
    print("correct!")
    score+=1
else:
    print("wrong answer!")

print("Your total score is ",score)
print("Your success rate is ",(score/6)*100," Percent")