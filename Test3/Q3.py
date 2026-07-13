'''3. Arrange Exam Marks
A teacher wants to display students' marks from the lowest to the
highest.
Write a program to sort the marks of all students in ascending order.'''





marks = list(map(int, input("Enter student marks: ").split()))
marks.sort()
print("Sorted Marks:", marks)
