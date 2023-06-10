import math

def fun():
    print('Hello')

fun()

def func(x,y=50):
    print(x,y)

func(10)
func(20,30)


def arg(*argv):
    for i in argv:
        print(i)
    
arg("Hello World")
arg("Hello World",'Geeks','For','Geeks')

def returnEven(list):
    for i in list:
        if i%2==0:
            yield i

list=[1,5,8,6,3,7]

for i in returnEven(list):
    print(i,end=" ")

print(sum(list))

import sys
print(sys.path)