#Display the front element of the queue without removing it

from collections import deque
queue_container = deque()

queue_container.insert(0,10)
queue_container.insert(1,20)
queue_container.insert(2,30)

print("The First element of the queue is:",queue_container[0])