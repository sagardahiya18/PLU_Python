'''2. Product ID Search
An e-commerce website stores product IDs in ascending order.
Write a program to find whether a customer-entered product ID exists in
the inventory. If it exists, display its index; otherwise, display "Product
Not Available."'''



def binary_search(product_ids, target):
    low, high = 0, len(product_ids) - 1
    while low <= high:
        mid = (low + high) // 2
        if product_ids[mid] == target:
            return mid
        elif product_ids[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

product_ids = list(map(int, input("Enter product IDs ").split()))
target = int(input("Enter product id "))

pos = binary_search(product_ids, target)

if pos != -1:
    print("Product found", pos)
else:
    print("Product Not Available")
