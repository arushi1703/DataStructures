class Node:
    def __init__(self,data,prev=None,next=None):
        self.data=data
        self.prev=prev
        self.next=next

class DoublyLinkedList:
    def __init__(self):
        self.head=None

    def insert_beg(self,data):
        node=Node(data)
        node.prev=None
        node.next=self.head

        if self.head is not None:
            self.head.prev=node
        self.head=node

    def append(self,data):
        node=Node(data)
        node.next=None
        last=self.head

        if self.head is None:
            node.prev=None
            self.head=node
            return
        while last.next is not None:
            last=last.next
        last.next=node
        node.prev=last

    def insert_index(self,data,index):
        current_node=self.head
        current_position=0
        while current_position != index-1:
            if current_node.next is None:
                print("Index out of bounds")
                return
            current_node=current_node.next
            current_position+=1
        newnode=Node(data,current_node,current_node.next)
        current_node.next=newnode
        newnode.next.prev=newnode
        print("Inserted",data,"at index",index)

    def display(self):
        temp=self.head
        print("None <->",end=' ')
        while temp:
            print(temp.data,"<->",end=' ')
            temp=temp.next
        print("None")

    def countelements(self):
        temp=self.head
        count=0
        while temp:
            count+=1
            temp=temp.next
        return count
            
l=DoublyLinkedList()
l.append(1)
l.append(2)
l.append(3)
l.display()
l.insert_beg(0)
l.insert_beg(-1)
l.display()
print("Number of elements:",l.countelements())
l.insert_index(10,4)
l.display()

        
