import random
answer = random.randint(1,100)
count = 0
while True:
    guess = int(input("猜?"))
    count += 1
    if guess > answer:
        print ("大了")
    elif guess < answer:
        print ("小了")
    else :
        print("对了,猜了",count,"次")
        break
