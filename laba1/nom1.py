a= int(input())
b= int(input())
c=int(input())

#1,2,3 строки - ввод чисел
if a>b and a>c:
  print(a)
elif b>a and b>c:
  print(b)
else:
  print(c)
#цикл определящий максимальное число
if a<b and a<c:
    print(a)
elif b<c and b<c:
    print(b)
else:
    print(c)
#цикл определящий минимальное число
if a==b==c:
    print("Одинаковые")
else:
    print("Разные")