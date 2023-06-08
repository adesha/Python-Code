x=1000000000000000000000000000000000000000000000000
print(x)
x=x+1
print(x)
print(100**100)

a = 9
b = 4
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a//b)
print(a**b)
print(a%b)

print(a>b)
print(a<b)
print(a==b)
print(a!=b)
print(a>=b)
print(a<=b)
print(a is b)
print(a is not b)

print(a&b)
print(a|b)
print(~a)
print(a^b)
print(a>>b)
print(a<<b)

list1=[10,4,8,7]
if a not in list1:
    print("It's not there")
if b in list1:
    print("It's there")

x,y=10,20
min=x if x<y else y
print(min)

print( (b, a) [a < b] )
print({True: a, False: b} [a < b])
print((lambda: b, lambda: a)[a < b]())

print(a,"is greater") if (a>b) else print(b,"is Greater")

min = a < b and a or b

print(min)

list1 = []
list2 = []
list3=list1

if (list1 == list2):
    print("True")
else:
    print("False")

if (list1 is list2):
    print("True")
else:
    print("False")

if (list1 is list3):
    print("True")
else:    
    print("False")

list3 = list3 + list2

if (list1 is list3):
    print("True")
else:    
    print("False")