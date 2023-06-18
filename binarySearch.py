def search(arr,x):
    i=0
    j=len(arr)-1
    while i<=j:
        mid=(i+j)//2
        if arr[mid]>x:
            j=mid-1
        elif arr[mid]<x:
            i=mid+1
        else:
            return mid
    return -1

a=[1,2,3,4,5,6,7,8,9,12]
target=6
print(search(a,target))