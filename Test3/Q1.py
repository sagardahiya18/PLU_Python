'''1. Student Roll Number Search
A teacher has stored the roll numbers of students in a list in the order
they registered. The list is not sorted.
Write a program to check whether a given roll number exists in the list.
If found, display its position; otherwise, print "Student Not Found'''




def searchroll(rollnum, target):
    length=len(rollnum)
    for i in range(length):
        if rollnum[i] == target:
            print("Roll number found at index :",i)
            break
    else:
        print("Student Not Found")

roll_numbers = list(map(int, input("Enter roll numbers separated by spaces: ").split()))
search = int(input("Enter roll number to search: "))
searchroll(roll_numbers, search)
