#Display all the elements of the queue in FIFO order
from collections import deque
queue_container = deque()

queue_container.insert(0,10)
queue_container.insert(1,20)
queue_container.insert(2,30)

print("The elements are in the FIFO ORDER :",queue_container)