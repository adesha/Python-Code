string=input()
list=string.split()
print(list)

n=int(input())

list=list(map(int,input().strip().split()))[:n]

print(list)

list=['hello','geeks','for','geeks']
list.sort()
print(list)

l1=[1,2,3,5]
l2=[3,6,8]
l3=l1+l2
print(l3)

l1=[1,2,3,5]
l2=[3,6,8]
l3=sorted(l1+l2)
print(l3)

l1=[1,2,3,5]
l2=[3,6,8]
l3=list(set(l1+l2))
print(l3)

l1.extend(l2)
print(l1)

l1=[1,2,3,5]
l2=[3,6,2,8]

l3=[]
for i in l1:
    if i in l1 and i in l2 and i not in l3:
        l3.append(i)

print(l3)