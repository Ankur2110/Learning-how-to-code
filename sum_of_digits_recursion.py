def sum_of_digits(n):
    assert n>=0 and int(n) == n, "Number has to be positive integer only"
    if n in [0,1]:
        return n
    else:
        return n%10 + sum_of_digits(n//10)
    
    
print (sum_of_digits(1167623))
