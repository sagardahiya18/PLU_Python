'''9. Library Book Search
A library has 10,000 books, and the Book IDs are already arranged in
ascending order.
Write a program to find a given Book ID efficiently.
Also mention which searching algorithm you used and why it is suitable.'''


'''We are going to use BINARY SEARCH ALGORITHM as this is the large data and dealing with large data is good with 
binary 

As Linear SEARCHING ALGORITHM check each and evry element to search the particular number 

In Binary Search the searching will be done by making the list in half part is larger then the particular number 
and the other half is smaller then if our number is smaller then go to the left side to search otherwise go to the right side
 


















'''

def binary_search(book_ids, target):
    low, high = 0, len(book_ids) - 1
    while low <= high:
        mid = (low + high) // 2
        if book_ids[mid] == target:
            return mid + 1 
        elif book_ids[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

book_ids = list(map(int, input("Enter Book IDs ").split()))
target = int(input("Enter Book ID to search: "))

pos = binary_search(book_ids, target)

if pos != -1:
    print("Book found at position:", pos)
else:
    print("Book Not Found")
