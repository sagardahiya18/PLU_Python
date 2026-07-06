#Display the top element of the stack without removing it.

from collections import deque
stack_container = deque()
stack_container.append(10)   
stack_container.append(20)
stack_container.append(30)
stack_container.append(40)
print("The top element of stack is",stack_container[-1])
