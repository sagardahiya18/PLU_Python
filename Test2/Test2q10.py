#Remove one element from the front of the queue and display the updated queue


from collections import deque
queue_container = deque()

queue_container.append(5)
queue_container.append(10)
queue_container.append(15)
queue_container.append(20)

queue_container.popleft()
print("The updated queue is: ",queue_container)
