'''5. Insert New Book by Price
A bookstore maintains a sorted list of book prices.
A new book arrives, and its price needs to be placed at the correct
position while keeping the list sorted.
Write a program to perform this task.'''


prices = list(map(int, input("Enter book prices:").split()))
new_price = int(input("Enter the new book price: "))

length=len(prices)
for i in range(length):
    if new_price < prices[i]:
        prices.insert(i, new_price)
        break
else:
    prices.append(new_price)

print("Updated Prices:", prices)



