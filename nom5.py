import random

n = [random.randint(1,100) for i in range(20)]



even_numbers = [num for num in n if num % 2 == 0]
print(even_numbers)

triple_numbers = [num for num in n if num % 3 == 0]
print(triple_numbers)

if n:
    avg = sum(n) / len(n)
print(avg)