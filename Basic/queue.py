#implementing queue using linked list
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class Queue:
    def __init__(self):
        self.__head=None
        self.__tail=None
        self.__count=0
    def enqueue(self,ele):
        newNode=Node(ele)
        if self.__head is None:
            self.__head=newNode
        else:
            self.__tail.next=newNode
        self.__tail=newNode
        self.__count+=1

    def dequeue(self):
        if self.__head is None:
            print("heyy!! , queue is empty")
            return
        else:
            data1=self.__head.data
            self.__head=self.__head.next
            self.__count-=1
            return data1
    def front(self):
        if self.__head is None:
            print("hey queue is empty")
        else:
            return self.__head.data
    def size(self):
        return self.__count
    def isempty(self):
        return self.size()==0


q=Queue()
q.enqueue(1) 
q.enqueue(2) 
q.enqueue(3)    
q.enqueue(4) 


while q.isempty() is False:
    print(q.front())
    q.dequeue()

q.front()