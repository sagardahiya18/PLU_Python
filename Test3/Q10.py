'''10. School Annual Report
A school has recorded the marks of 50 students.
Write a program that:
Sorts the marks in ascending order.
Accepts a mark from the user.
Checks whether that mark exists in the sorted list.
Displays the position if found; otherwise, prints "Mark Not Found.'''



def binary_search(marks, target):
    low, high = 0, len(marks) - 1
    while low <= high:
        mid = (low + high) // 2
        if marks[mid] == target:
            return mid + 1   
        elif marks[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

marks = list(map(int, input("Enter marks: ").split()))
marks.sort()
print("Sorted Marks (Ascending):", marks)

target = int(input("Enter a mark to search: "))
pos = binary_search(marks, target)

if pos != -1:
    print("Mark found at position:", pos)
else:
    print("Mark Not Found")
