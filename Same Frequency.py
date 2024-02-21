# Define a function which takes two lists as parameters and check if two given lists have the same frequency of elements.

# Example:

#     list1 = [1, 2, 3, 2, 1]
#     list2 = [3, 1, 2, 1, 3]
#     check_same_frequency(list1, list2)

# Output:

# False 



def check_same_frequency(list1, list2):
    list1.sort()
    list2.sort()
    if list1 == list2:
        return True
    else:
        return False
