# Linked List
class node:
    def __init__(self,data):
        self.data=data
        self.next=None

class linkedList:
    def __init__(self):
        self.head=None

    def printlist(self):
        temp=self.head
        while temp:
            print(temp.data)
            temp=temp.next

if __name__=='__main__':
    llist=linkedList()
    llist.head=node(1)
    second=node(2)
    third=node(3)

    llist.head.next=second
    # llist.head.next.next=third
    second.next=third
    llist.printlist()

# Circular Linked List
class node:
    def __init__(self,data):
        self.data=data
        self.next=None

class linkedList:
    def __init__(self):
        self.head=None

    def printlist(self):
        temp=self.head
        while True:
            print(temp.data)
            temp=temp.next
            if temp==self.head:
                break

if __name__=='__main__':
    llist=linkedList()
    llist.head=node(1)
    second=node(2)
    third=node(3)

    llist.head.next=second
    # llist.head.next.next=third
    second.next=third
    third.next=llist.head
    llist.printlist()

# Double Linked List
class node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None

class linkedList:
    def __init__(self):
        self.head=None

    def printlist(self):
        temp=self.head
        while temp:
            print(temp.data)
            temp=temp.next

if __name__=='__main__':
    llist=linkedList()
    llist.head=node(1)
    second=node(2)
    third=node(3)

    llist.head.next=second
    # llist.head.next.next=third
    second.next=third
    second.prev=llist.head
    third.prev=second
    llist.printlist()