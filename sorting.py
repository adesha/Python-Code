# # Bubble sort
# def bubbleSort(arr):
#     for i in range(0,len(arr)-1):
#         for j in range(i+1,len(arr)):
#             if arr[i]>arr[j]:
#                 arr[i],arr[j]=arr[j],arr[i]

#     return arr

# # a=[5,9,7,1,2,5]
# a=[1,4,2,3,7,5]
# ans=bubbleSort(a)
# print(a)
# print(ans)

# # Selection sort
# def selectionSort(arr):
#     for i in range(0,len(arr)-1):
#         min=100000000
#         k=0
#         for j in range(i+1,len(arr)):
#             if arr[j]<min:
#                 min=arr[j]
#                 k=j
#         if min<arr[i]:
#             arr[i],arr[k]=arr[k],arr[i]
#     return arr
# # a=[5,9,7,1,2,5]
# a=[1,4,2,3,7,5]
# print(a)
# ans=selectionSort(a)
# print(ans)

# # Insertion sort
# def insertionSort(arr):
#     for i in range(1,len(arr)):
#         key=arr[i]
#         j=i-1
#         while j>=0 and arr[j]>key:
#             arr[j+1]=arr[j]
#             j=j-1
#         arr[j+1]=key
#     return arr

# # a=[5,9,7,1,2,5]
# a=[1,4,2,3,7,5]
# print(a)
# ans=insertionSort(a)
# print(ans)

# Merge sort
def mergeSort(arr,l,r):
    if l<r:
        mid=(l+r)//2
        mergeSort(arr,l,mid)
        mergeSort(arr,mid+1,r)
        merge(arr,l,mid,r)

def merge(arr,l,mid,r):
    firstHalf=arr[:mid]
    secondHalf=arr[mid:]
    i=j=k=0
    while i<len(firstHalf) and j<len(secondHalf):
        if firstHalf[i]>secondHalf[j]:
            arr[k]=secondHalf[j]
            j+=1
        else:
            arr[k]=firstHalf[i]
            i+=1
        k+=1
    while i<len(firstHalf):
        arr[k]=firstHalf[i]
        i+=1
        k+=1
    while j<len(secondHalf):
        arr[k]=secondHalf[j]
        j+=1
        k+=1
    
# a=[5,9,7,1,2,5]
# a=[1,4,2,3,7,5]
a=[1]
print(a)
mergeSort(a,0,len(a))
print(a)

