# Задача 10 про моентки. 
# 1. вариант решения
"""
n = int(input('напишите количество монет на столе '))
x = int(input("количество монет с орлом вверх "))
if x == 0:
    print(f"количество переворотов {0}")
else:
    print(f"количество переворотов {n-x}")
"""
# 2. Вариант решения
"""
n = int(input('напишите количество монет на столе '))
count_back = 0
count_front = 0
print("если монета орлом вврех, напишите 1, если  решкой - 0")

for i in range(n):
    x = int(input())
    if x == 0:
        count_back+=1
    else:
        count_front += 1

if count_front > count_back:
        print(f"количество переворотов {count_back}")
else:
        print(f"количество переворотов {count_front}")
"""
# Задача 12. Числа
"""
print("Напишите сумму чисел = ")
summa = int(input())
print("Напишите произведение чисел = ")
multi = int(input())
for i in range(summa):
    for j in range(multi):
        if summa == i+j and multi==i*j:
            print(f"Первое число = {i} Второе число = {j}")
"""
# Задача 14

print("напишите число, до которого трбеуется возводить в степень")
n = int(input())
y = 1
while n>=y:
    print(y)
    y *= 2