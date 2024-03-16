# captalizeFirst

# Write a recursive function called capitalizeFirst. Given an array of strings, capitalize the first letter of each string in the array.

# Example

#     capitalizeFirst(['car', 'taco', 'banana']) # ['Car','Taco','Banana']



def capitalizeFirst(arr):
    if len(arr)==0:
        return []
    else:
        return [arr[0].capitalize()] + capitalizeFirst(arr[1:])