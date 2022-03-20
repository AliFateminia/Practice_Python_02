# practice 2_1 >>> wihle
sm = 0
while True:
    x = input("Enter your number : ")
    if x == "exit":
        print("sum :", sm)
        break
    sm = sm + float(x)
