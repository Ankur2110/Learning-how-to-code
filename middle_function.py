# takes a list and returns a new list that contains all but the first and last elements
def middle(list):
    new_list=[]
    for i in range(1,len(list)-1):
        new_list.append(list[i])
    return new_list



print(middle([1,2,3,4,5,6,1,35,1]))
