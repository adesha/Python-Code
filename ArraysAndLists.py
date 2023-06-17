# Linear - Array,Stack,Queue,Linked list,Hash table 
# Non-Linear - Trees, Graph,

import array as arr

a=arr.array('i',[1,2,3])
print(a)
for i in range(0,3):
    print(a[i],end=" ")

print('')

a.insert(1,4)
print(a)

a.pop()
print(a)
a.pop(1)
print(a)
a[1]=6
print(a)
print(len(a))
list=[1,2,3]
print(len(list))
list.append(4)
print(list)
list.insert(0,6)
print(list)
list.extend([8,9,7])
print(list)
list.remove(6)
print(list)
list.pop()
print(list)
list.pop(4)
print(list)