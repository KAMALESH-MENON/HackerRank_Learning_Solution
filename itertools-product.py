from itertools import product

a = list(map(int, input().split()))
b = list(map(int, input().split()))
r = product(a,b)

#print(tuple(r))
for i in r:
    print(i, end=" ")