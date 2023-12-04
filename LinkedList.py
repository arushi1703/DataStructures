class Node:
    def __init__(self,data,next):
        self.data=data
        self.next=next

class SingleList:
    head=None
    tail=None

    def append(self,data):
        node=Node(data,None)
        if self.head is None:
            self.head=self.tail=node
        else:
            self.tail.next=node
            self.tail=node

    def insert_beg(self,data):
        node=Node(data,self.head)
        self.head=node
    
    def display(self):
        print("Linked List:")
        current_node=self.head
        while current_node is not None:
            print(current_node.data,"->",end=' ')
            current_node=current_node.next
        print(None)

    def countelements(self):
        count=0
        current_node=self.head
        while current_node is not None:
            count+=1
            current_node=current_node.next
        return count
        

l=SingleList()
l.append(1)
l.append(2)
l.append(3)
l.display()
l.insert_beg(0)
l.insert_beg(-1)
l.display()
print("Number of elements:",l.countelements())
