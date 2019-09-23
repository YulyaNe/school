print('Введите три числа:')
from random import*
a=randint(0,9)
b=randint(0,9)
c=randint(0,9)
print(a, b, c,sep=" ")
if a==b==c:
     print('Все числа одинаковые.')
elif a==c:
     print('Два числа одинаковые.')
elif a==b:
     print('Два числа одинаковые.')
elif b==c:
    print('Два числа одинаковые.')
else:
    print('Нет одинаковых чисел.')
    
