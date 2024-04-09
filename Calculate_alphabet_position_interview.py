# Given a string containing alphanumeric enteries, return another string, where letters are replaced by their position in alphabet


import string

def alphabet(input_string):
    output =""
    for item in input_string:
        if item.isalpha():
            output +=  str(string.ascii_lowercase.index(item) +1)
        else:
            output += item
    return output



print(alphabet("abczz"))