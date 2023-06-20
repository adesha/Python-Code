# empty(),size(),pop(),push(x),top()

stack=[]

def push(x):
    stack.append(x)

def pop():
    if len(stack)>=1:
        stack.pop()
    else:
        print('Stack is empty')

def top():
    if len(stack)>=1:
        return stack[len(stack)-1]
    else:
        return 'Stack is empty'
    
def empty():
    if len(stack)>=1:
        return False
    return True    

def size():
    return len(stack)

push(1)
push(2)
push(3)
print(stack)
pop()
# pop()
# pop()
# pop()
print(stack)
print(top())
print(stack)
print(empty())
print(size())
print(stack)