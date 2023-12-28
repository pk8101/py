#optimized code for linked list to take inputs
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
            tail=newNode
        else:
            tail.next=newNode
            tail=newNode
            
    return head
#to find length of the linked list
def lengthll(head):
    count=0
    while head is not None:
        count=count+1
        head=head.next
    return count
#to insert the value at the specific position in a linked list
def insertatI(head,i,data):

    if i<0 or i>lengthll(head):
        return head

    count=0
    prev=None
    curr=head
    while i>count :
        prev=curr
        curr=curr.next
        count=count+1
    newNode=Node(data)
    if prev is not None:
        prev.next=newNode
    else:
        head=newNode
    newNode.next=curr
    return head
#insert data recursively
def inserdataatir(head,i,data):
    if i<0:
        return head
    if i==0:
        newNode=Node(data)
        newNode.next=head
        return newNode
    if head is None:
        return None
    smallhead=inserdataatir(head.next,i-1,data)
    head.next=smallhead

    return head
# reverse of linked list using recursion
def reversel(head):
    if head is None or head.next is None:
        return head
    
    smallHead=reversel(head.next)
    curr=smallHead
    while curr.next is not None:
        curr=curr.next
    curr.next=head
    head.next=None
    return smallHead
# reverse of linked list using recursion (optimized using tail)
def reverse2(head):
    if head is None or head.next is None:
        return head,head
    
    smallHead,tail=reverse2(head.next)
    tail.next=head
    head.next=None
    return smallHead,head
def printll(head):
    while head is not None:
        print(str(head.data)+"->",end="")
        head=head.next
    print("none")
    return 


head=takeinput()
printll(head)
head=insertatI(head,2,20)
printll(head)
head=insertatI(head,3,5)
printll(head)
inserdataatir(head,4,30)
printll(head)
# head=reversel(head)
# printll(head)
head,tail=reverse2(head)
printll(head)