def decimal_to_binary(n):
    assert int(n) == n, "Input should be an integer only"
    if n==0:
        return 0
    else:
        return n%2 +10*decimal_to_binary(n//2)
    

print(decimal_to_binary(4))