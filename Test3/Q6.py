'''6. Employee Salary Report
An HR department has employee salary records collected from two different
branches.
Write a program to combine both lists and display all salaries in
ascending order.'''

branch1 = list(map(int, input("Enter salaries of Branch 1  ").split()))
branch2 = list(map(int, input("Enter salaries of Branch 2  ").split()))

combine = branch1 + branch2
combine.sort()

print("All Salaries", combine)
