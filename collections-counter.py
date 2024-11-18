from collections import Counter
no_of_shoes = int(input())

list_of_shoes = list(map(int, input().split()))

count_shoe = dict(Counter(list_of_shoes))

no_of_customers = int(input())


total = 0
for customer in range (no_of_customers):
    shoe_size, shoe_price = map(int, input().split())
    
    if count_shoe.get(shoe_size):
        count_shoe[shoe_size] -= 1
        total += shoe_price 
print(total)
