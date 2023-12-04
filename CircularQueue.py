def enqueue(e):
    global front,rear,size
    if isEmpty(): #if e is the first element
        front=rear=0
    elif(rear+1)%size == front: #if queue is full
        print("Queue overflow")
    else: #else add the element to the queue
        rear=(rear+1)%size
    queue[rear]=e

def dequeue():
    global front,rear,size
    if isEmpty(): #if queue is empty
        print("Queue underflow")
        return
    e=first()
    if front==rear: #if there is only one element
        front=rear=-1
    else:
        front=(front+1)%size
    return e

def isEmpty():
    global front, rear
    if front==-1 and rear==-1:
        return True
    return False

def first():
    if isEmpty():
        print("Queue is empty")
        return
    return queue[front]

def display():
    global front,rear,size
    if isEmpty():
        print("Queue is empty")
        return
    elif rear>=front:
        for i in range(front,rear+1):
            print(queue[i], end=' ')
    else:
        for i in range(front,size):
            print(queue[i], end=' ')
        for i in range(0,rear+1):
            print(queue[i], end=' ')
    print()

def countelements():
    global front,rear,size
    count=0
    if isEmpty():
        return 0
    elif rear>=front:
        for i in range(front,rear):
            count+=1
    else:
        for i in range(front,size):
            count+=1
        for i in range(0,rear+1):
            count+=1
    return count
    
    
size=3
front=rear=-1
queue=[None]*size
for i in range(1,4):
    enqueue(i)
display()
dequeue()
dequeue()
enqueue(4)
display()
print("First Element:",first())
print("No. of elements:",countelements())
