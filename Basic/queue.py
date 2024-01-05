#inbulit stack
# we can use stack in two ways 1.List itself used as a stack
# 2.in queue there is a class that follow Lifo order class_name-->(LifoQueue())

# way -->1: List
stack=[]
stack.append(1)
stack.append(2)
stack.append(3)
stack.append(4)
stack.pop()
stack.pop()
stack.pop()
print(stack)

# way-->2: using class in queue
#the below code is getting error but we should implemet the inbulit stack like this only


# import queue
# q=queue.LifoQueue
# q.put(1)
# q.put(2)
# q.put(3)

# while not q.empty():
#     print(q.get())


#inbulit queue implemented
# import queue
# q=queue.Queue()
# q.put(1)
# q.put(2)
# q.put(3)

# while not q.empty():
#     print(q.get())