#Create a queue and insert the values 10, 20, 30, 40

from collections import deque
queue_container = deque()

queue_container.insert(0,10)
queue_container.insert(1,20)
queue_container.insert(2,30)

print("The elements of the queue are:",queue_container)