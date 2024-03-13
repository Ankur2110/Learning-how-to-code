def fibobacci(n)
    assert n>=0 and int(n) ==n, "Fibonacci number should be non-negative integer only"
    if n in [0,1]:
        return n
    else:
        return fibobacci(n-1) + fibobacci(n-2)
    
