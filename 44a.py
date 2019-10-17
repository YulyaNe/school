n=int(input())
summa = 0
while n%10!=0:
    summa=summa+n%10
    n=int(n / 10)
print(summa)

