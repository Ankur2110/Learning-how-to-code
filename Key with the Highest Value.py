# Define a function which takes a dictionary as a parameter and returns the key with the highest value in a dictionary.

# Example:

#     my_dict = {'a': 5, 'b': 9, 'c': 2}
#     max_value_key(my_dict))

# Output:

# b 


def max_value_key(my_dict):
    value_list = list(my_dict.values())
    value_list.sort()
    for key in my_dict:
        if my_dict[key] == value_list[-1]:
            return key
            

def max_value_key_1(my_dict):
    return max(my_dict, key=my_dict.get)