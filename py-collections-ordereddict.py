# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import OrderedDict
ordered_dictionary = OrderedDict()
n = int(input())
for i in range(n):
    name, price = input().rsplit(' ',1)
    
    if name not in ordered_dictionary:
        ordered_dictionary[name] = int(price)
    else:
        ordered_dictionary[name] += int(price)

for name, price in ordered_dictionary.items(): 
    print(f'{name} {price}')