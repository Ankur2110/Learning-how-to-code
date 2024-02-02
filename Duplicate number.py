#Write a function to remove the duplicate numbers on given integer array/list.


def duplicate_number(list):
    unique_list =[]
    seen=[]
    for i in range(len(list)):
        if list[i] not in seen:
            seen.append(list[i])
            unique_list.append(list[i])
    return unique_list

print (duplicate_number([1,2,3,3,3,3,3,3,3,4,5,6,4,4,5]))

