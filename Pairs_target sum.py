#Write a function to find all pairs of an integer array whose sum is equal to a given number. Do not consider commutative pairs. 

def pair_sum(arr,target):
    pairs=[]
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i]+arr[j] == target:
                pairs.append((arr[i],arr[j]))
    return pairs



print (pair_sum([4,8,9,3,10,2,2,2,11,1,11],12))
