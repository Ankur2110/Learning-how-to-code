def bubble_sort(arr):
    for i in range(len(arr)-1):
        stopper =0
        for j in range(len(arr)-i-1):
            if arr[j] > arr[j+1]:
                stopper =1
                arr[j], arr[j+1] = arr[j+1], arr[j]
        if stopper==0:
            return arr
    return arr



print(bubble_sort([1,4,3,9,8,7,5]))
