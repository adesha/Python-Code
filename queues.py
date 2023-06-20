# Enqueue(x), Dequeue(), Front(), Rear()
queue=[]

def enqueue(x):
    queue.append(x)

def dequeue():
    if len(queue)>=1:
        queue.pop(0)
    else:
        print('Queue is empty')
    
def front():
    if len(queue)>=1:
        return queue[0]
    else:
        return 'Queue is empty'
    
def rear():
    if len(queue)>=1:
        return queue[len(queue)-1]
    else:
        return 'Queue is empty'
    

enqueue(1)
enqueue(2)
enqueue(3)
print(queue)
dequeue()
# dequeue()
# dequeue()
# dequeue()
print(queue)
print(front())
print(queue)
print(rear())
print(queue)