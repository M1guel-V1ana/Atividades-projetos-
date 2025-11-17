'''
n = int(input())

l = [x for x in range(n +1)]

l1 = [x for x in l if x % 2 == 0]
l2 =  [x for x in l if x % 2 != 0]
print(l)
print(l1)
print(l2)
'''

b = int(input(": "))
l =[]
for i in range(b):
    n = input("digite algo: ")
    l.append(n)

print(l)
