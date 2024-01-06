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
btn1=BinaryTreeNode(1) #root node
btn2=BinaryTreeNode(2) #left node
btn3=BinaryTreeNode(3) #right node

btn1.left=btn2
btn1.right=btn3


printTree(btn1)