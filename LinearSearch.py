def search(arr,x):
    for i in arr:
        if i==x:
            return True
    return False

list=[1,5,2,3,6,9,7,4]
target=3
ans=search(list,target)
if(ans==True):
    print('Number Found')
else:
    print('Number Not Found')