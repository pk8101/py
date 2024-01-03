#implementing queue using array
class Queue:
    def __init__(self):
        self.__arr=[]
        self.__count=0
        self.__front=0
    def enqueue(self,data):
        self.__arr.append(data)
        self.__count+=1

    def dequeue(self):
        if self.__count==0:
            return -1
        ele=self.__arr[self.__front]
        self.__front+=1
        self.__count-=1
        return ele
    def front(self):
        if self.__count==0:
            return -1
        return self.__arr[self.__front]
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
