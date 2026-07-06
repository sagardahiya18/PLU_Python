#Check whether a stack is empty and display an appropriate message

from collections import deque
stack=deque()



if len(stack) ==0:         #len is used to check the length of the stack 
    print("stack is empty")
else:
    print ("stack has some value",stack)
    