''' print('напишите длину первого списка ')
n = int(input())
list_first=[]
for i in range(n):
    list_first.append(int(input()))
list_first=set(list_first)
print('напишите длину второго списка ')
m = int(input())
list_second=[]
for i in range(m):
    list_second.append(int(input()))
list_second=set(list_second)
print(*list_first)
print(*list_second)
z = list_first.intersection(list_second)
print(z)
'''

n = int(input("напишите количество грядок = "))
ugoda=[]
for i in range(n):
    ugoda.append(int(input()))
print(ugoda)
summa_3_grydok=[]
for i in range(n-1):
    summa_3_grydok.append(ugoda[i-1]+ugoda[i]+ugoda[i+1])
summa_3_grydok.append(ugoda[-2]+ugoda[-1]+ugoda[0])
print(summa_3_grydok)
print(max(summa_3_grydok))
