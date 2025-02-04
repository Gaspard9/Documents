num = int(input("enter a number: "))

flag = False

if num > 1:
    #check for factors
    for i in range(2, num):
        if (num % i) == 0:
            flag = True
            break

if flag:
    print(num, "is a not prime number")
else:
    print(num, "is a prime number")