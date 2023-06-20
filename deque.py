from collections import deque

queue=deque(['gfg','hello',123])
print(queue)

queue.append(456)
print(queue)
queue.appendleft('world')
print(queue)
queue.pop()
print(queue)
queue.popleft()
print(queue)

# append():- This function is used to insert the value in its argument to the right end of the deque.
# appendleft():- This function is used to insert the value in its argument to the left end of the deque.
# pop():- This function is used to delete an argument from the right end of the deque.
# popleft():- This function is used to delete an argument from the left end of the deque.
# index(ele, beg, end):- This function returns the first index of the value mentioned in arguments, 
#   starting searching from beg till end index.
# insert(i, a) :- This function inserts the value mentioned in arguments(a) at index(i) specified in arguments.
# remove():- This function removes the first occurrence of value mentioned in arguments.
# count():- This function counts the number of occurrences of value mentioned in arguments.
# extend(iterable):- This function is used to add multiple values at the right end of the deque. 
#   The argument passed is iterable.
# extendleft(iterable):- This function is used to add multiple values at the left end of the deque. 
#   The argument passed is iterable. Order is reversed as a result of left appends.
# reverse():- This function is used to reverse the order of deque elements.
# rotate():- This function rotates the deque by the number specified in arguments. 
#   If the number specified is negative, rotation occurs to the left. Else rotation is to right.