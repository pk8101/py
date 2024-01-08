# Binary contain maximum of two nodes either(0,1,2)nodes
# start node cosider as root node it contains left ,right reference for the child nodes
# trees does not contain an cycles

# implementing basic binary tree
class BinaryTreeNode:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
def printTree(root):
    if root==None:
        return
    print(root.data)
    printTree(root.left)
    printTree(root.right)

def printTreeDetailed(root):
    if root== None:
        return
    print(root.data,end=":")
    if root.left != None:
        print("L",root.left.data,end=",")
    if root.right != None:
        print("R",root.right.data,end="")
    print()
    printTreeDetailed(root.left)
    printTreeDetailed(root.right)

def takeinput():
    rootData=int(input())
    if rootData==-1:
        return None
    root=BinaryTreeNode(rootData)
    leftTree=takeinput()
    rightTree=takeinput()
    root.left=leftTree
    root.right=rightTree
    return root

def numNodes(root):
    if root==None:
        return 0
    leftCount=numNodes(root.left)
    rightCount=numNodes(root.right)
    return 1+leftCount+rightCount

def largeNode(root):
    if root == None:
        return -1
    leftLarge=largeNode(root.left)
    rightLarge=largeNode(root.right)
    largest=max(leftLarge,rightLarge,root.data)
    return largest
def noOfLeafNodes(root):
    if root==None:
        return 0
    if root.left==None and root.right==None:
        return 1
    noOfLeftNode=noOfLeafNodes(root.left)
    noOfRightNode=noOfLeafNodes(root.right)
    return noOfLeftNode+noOfRightNode
def depthOfK(root,k):
    if root==None:
        return 0
    if k==0:
        print(root.data)
        return
    depthOfK(root.left,k-1)
    depthOfK(root.right,k-1)

def depthOfKV2(root,k,d=0):
    if root==None:
        return 0
    if k==d:
        print(root.data)
        return
    depthOfKV2(root.left,k,d+1)
    depthOfKV2(root.right,k,d+1)

def removeLeaf(root):
    if root==None:
        return None
    if root.left==None and root.right==None:
        return None
    root.left=removeLeaf(root.left)
    root.right=removeLeaf(root.right)
    return root

#balance of the tree is true or false
def height(root):
    if root==None:
        return 0
    return 1+max(height(root.left),height(root.right))
def isBalanced(root):
    if root==None:
        return True
    lh=height(root.left)
    rh=height(root.right)
    if lh-rh>1 or rh-lh>1:
        return False
    leftBalance=isBalanced(root.left)
    rightBalance=isBalanced(root.right)
    if leftBalance and rightBalance:
        return True
    else:
        return False



root=takeinput()
printTree(root)
print()
printTreeDetailed(root)
print("no of node:",numNodes(root))
print("large node:",largeNode(root))
print("no of leaf node:",noOfLeafNodes(root))
print("data of kth Nodes:")
depthOfK(root,1)
print("data of kth Nodes using depthOfK version -2 method:")
depthOfKV2(root,1)
print("Tree after removing leaf Nodes:")
root=removeLeaf(root)
printTreeDetailed(root)

print(isBalanced(root))