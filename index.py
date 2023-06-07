print('hello')
a=3
print(a)
a='world'
print(a)
print(a[0])
print (type(type(int)))
a = 5
print("Type of a: ", type(a))

b = 5.0
print("\nType of b: ", type(b))

c = 2 + 4j
print("\nType of c: ", type(c))

list=[]
print(list)
list=['geeks','for','geeks']
print(list)
print(list[0])
print(list[0][1])
list=[['abc','xyz'],'mno']
print(list)
print(list[0])
print(list[0][0])
print(list[0][0][1])

tuple1=()
print(tuple1)
tuple1 = ('Geeks', 'For')
print(tuple1)
print(tuple1[0])
#tuple1[0]='Geek'
print(tuple1)
print(tuple1[0])

list1 = [1, 2, 4, 5, 6]
print(list1)
print(tuple(list1))

Tuple1 = (0, 1, 2, 3)
Tuple2 = ('python', 'geek')
Tuple3 = (Tuple1, Tuple2)
print(Tuple3)

print(type(True))
print(type(False))

# print(type(true))

set1=set()
print(set1)
set1=set('GeeksForGeek')
print(set1)
set1=set(['geeks','for','geeks','Geeks'])
print(set1)
for i in set1:
    print(i)

Dict={}
print(Dict)
Dict = {1: 'Geeks', 2: 'For', 3: 'Geeks'}
print(Dict)

Dict = {'Name': 'Geeks', 1: [1, 2, 3, 4]}
print(Dict)

print(Dict['Name'])
print(Dict[1])
print(Dict.get(1))
print(Dict.get('Name'))