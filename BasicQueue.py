def enqueue(e):
    queue.append(e)

def dequeue():
    if isEmpty():
        print("Queue is empty")
    e=first()
    del queue[0]
    return e

def isEmpty():
    if queue:
        return False
    return True

def first():
    if isEmpty():
        return
    return queue[0]

def display():
    print(queue)

queue=[]
enqueue(1)
enqueue(2)
enqueue(3)
enqueue(4)
enqueue(5)
display()
print("Popped Element:",dequeue())
print("Popped Element:",dequeue())
display()
