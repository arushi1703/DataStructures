class Node:
    def __init__(self,data):
        self.val=data
        self.left=None
        self.right=None

def insert(root,newnode):
    if root is None:
        root=newnode
    else:
        if root.val<newnode.val:
            if root.right is None:
                root.right=newnode
            else:
                insert(root.right,newnode)
        else:
            if root.left is None:
                root.left=newnode
            else:
                insert(root.left,newnode)

def inorder(root):
    if root:
        inorder(root.left)
        print(root.val, end=' ')
        inorder(root.right)

def preorder(root):
    if root:
        print(root.val,end=' ')
        preorder(root.left)
        preorder(root.right)

def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.val, end=' ')

r=Node(100)
insert(r,Node(20))
insert(r,Node(10))
insert(r,Node(50))
insert(r,Node(120))
insert(r,Node(102))
insert(r,Node(180))
print("Inorder:")
inorder(r)
print("\nPreorder:")
preorder(r)
print("\nPostorder:")
postorder(r)
