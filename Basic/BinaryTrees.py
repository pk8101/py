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

root=takeinput()
printTree(root)
print()
printTreeDetailed(root)
print(numNodes(root))