#Pop one element from the stack and display the updated stack

from collections import deque
stack_container = deque()
stack_container.append(10)   
stack_container.append(20)
stack_container.append(30)
stack_container.append(40)
stack_container.pop()     #will pop the top element
print("The elements of stack are",stack_container)