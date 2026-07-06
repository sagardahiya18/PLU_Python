#Create an empty stack and push the values 5, 10, 15, 20 into it. Display the stack


from collections import deque
stack_container = deque()
stack_container.append(10)   
stack_container.append(20)
stack_container.append(30)
stack_container.append(40)
print("The elements of stack are",stack_container)