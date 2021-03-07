#冒泡
def BubbleSort(lst):
    n=len(lst)
    if n<=1:
        return lst
    for i in range (0,n):
        for j in range(0,n-i-1):
            if lst[j]>lst[j+1]:
                (lst[j],lst[j+1])=(lst[j+1],lst[j])
    return lst

#快排

def QuickSort(lst):
    def partition(arr, left, right):
        key = left  
        while left < right:
            while left < right and arr[right] >= arr[key]:
                right -= 1
            while left < right and arr[left] <= arr[key]:
                left += 1
            (arr[left], arr[right]) = (arr[right], arr[left])
 
        (arr[left], arr[key]) = (arr[key], arr[left])
        return left
 
    def quicksort(arr, left, right):  
        if left >= right:
            return
        mid = partition(arr, left, right)
        quicksort(arr, left, mid - 1)
        quicksort(arr, mid + 1, right)

# 选择排序
def SelectSort(lst):
    n=len(lst)
    if n<=1:
        return lst
    for i in range(0,n-1):
        minIndex=i
        for j in range(i+1,n):          
            if lst[j]<lst[minIndex]:
                minIndex=j
        if minIndex!=i:                   
            (lst[minIndex],lst[i])=(lst[i],lst[minIndex])
    return lst

# 归并排序
def MergeSort(lst):
    def merge(arr,left,mid,right):
        temp=[]     
        i=left          
        j=mid+1   
        while i<=mid and j<=right:
            if arr[i]<=arr[j]:
                temp.append(arr[i])
                i+=1
            else:
                temp.append(arr[j])
                j+=1
        while i<=mid:
            temp.append(arr[i])
            i+=1
        while j<=right:
            temp.append(arr[j])
            j+=1
        for i in range(left,right+1):   
            arr[i]=temp[i-left]
    def mSort(arr,left,right):
        if left>=right:
            return
        mid=(left+right)//2
        mSort(arr,left,mid)
        mSort(arr,mid+1,right)
        merge(arr,left,mid,right)
 
    n=len(lst)
    if n<=1:
        return lst
    mSort(lst,0,n-1)
    return lst

