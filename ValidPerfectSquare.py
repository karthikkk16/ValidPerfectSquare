def ValidPerfectSquare(number):
    i=1
    while (i * i)<=number:
        if (i*i==number):
            return True
        i+=1
    return False
number=int(input())
print(ValidPerfectSquare(number))