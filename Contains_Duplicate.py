#Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

def contains_duplicate(nums):
    set1 = set(nums)
    if len(set1) == len (nums):
        return False
    else:
        return True


