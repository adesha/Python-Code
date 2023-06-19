# Bubble sort
def bubbleSort(arr):
    for i in range(0,len(arr)-1):
        for j in range(i+1,len(arr)):
            if arr[i]>arr[j]:
                arr[i],arr[j]=arr[j],arr[i]

    return arr

# a=[5,9,7,1,2,5]
a=[1,4,2,3,7,5]
ans=bubbleSort(a)
print(a)
print(ans)

# Selection sort
def selectionSort(arr):
    for i in range(0,len(arr)-1):
        min=100000000
        k=0
        for j in range(i+1,len(arr)):
            if arr[j]<min:
                min=arr[j]
                k=j
        if min<arr[i]:
            arr[i],arr[k]=arr[k],arr[i]
    return arr
# a=[5,9,7,1,2,5]
a=[1,4,2,3,7,5]
print(a)
ans=selectionSort(a)
print(ans)

# Insertion sort
def insertionSort(arr):
    for i in range(1,len(arr)):
        key=arr[i]
        j=i-1
        while j>=0 and arr[j]>key:
            arr[j+1]=arr[j]
            j=j-1
        arr[j+1]=key
    return arr

# a=[5,9,7,1,2,5]
a=[1,4,2,3,7,5]
print(a)
ans=insertionSort(a)
print(ans)