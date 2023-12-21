class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

def takeinput():
    inputlist=[int(ele)for ele in input().split()]
    head=None
    for currentdata in inputlist:
        if currentdata==-1:
            break
        newNode=Node(currentdata)
        

        if head is None:
            head=newNode
        else:
            currenhead=head
            while currenhead.next is not None:
                currenhead=currenhead.next
            
            currenhead.next=newNode

    return head

def printll(head):
    while head is not None:
        print(str(head.data)+"->",end="")
        head=head.next
    print("none")
    return 


head=takeinput()
printll(head)