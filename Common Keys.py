# Define a function with takes two dictionaries as parameters and merge them and sum the values of common keys.

# Example:

#     dict1 = {'a': 1, 'b': 2, 'c': 3}
#     dict2 = {'b': 3, 'c': 4, 'd': 5}
#     merge_dicts(dict1, dict2)

# Output:

#     {'a': 1, 'b': 5, 'c': 7, 'd': 5}

def merge_dicts(dict1, dict2):
    output_dict =dict1.copy()
    for key in dict2:
        output_dict[key] = output_dict.get(key,0) + dict2.get(key)
    return output_dict



def merge_dicts_1(dict1, dict2):
    result = dict1.copy()
    for key, value in dict2.items():
        result[key] = result.get(key, 0) + value
    return result