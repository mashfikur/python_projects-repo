n=list(map(int,input().split()))

count_even=0
count_odd=0
even=[]
non=[]


for x in n:
    if x%2==0:
        count_even+=1
        even.append(x)


    elif x%2!=0:
        count_odd+=1
        non.append(x)


print(f'The amount of even numbers are : {count_even}')
print(f'The amount of odd numbers are : {count_odd}')
print(f'The even numbers are :{even}')
print(f'The odd numbers are :{non}')