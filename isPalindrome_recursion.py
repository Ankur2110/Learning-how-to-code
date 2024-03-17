# Write a recursive function called isPalindrome which returns true if the string passed to it is a palindrome (reads the same forward and backward). Otherwise it returns false.

# Examples

#     isPalindrome('awesome') # false
#     isPalindrome('foobar') # false
#     isPalindrome('tacocat') # true
#     isPalindrome('amanaplanacanalpanama') # true
#     isPalindrome('amanaplanacanalpandemonium') # false



def isPalindrome(strng):
    if len(strng)<=1:
        return True
    elif strng[0]==strng[-1]:
        return isPalindrome(strng[1:-1])
    else:
        return False