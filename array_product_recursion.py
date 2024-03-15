# Write a function called productOfArray which takes in an array of numbers and returns the product of them all.

# Examples

#     productOfArray([1,2,3]) #6
#     productOfArray([1,2,3,10]) #60



def productOfArray(arr):
    if not arr:
        return 1
    else:
        return arr[0]*productOfArray(arr[1:])