def lonelyinteger(a):
    sorted_input = sorted(a)
    pointer = 0
    for _ in range(len(sorted_input)//2):
        if sorted_input[pointer] != sorted_input[pointer+1]:
            return sorted_input[pointer]
        pointer +=2
    return sorted_input[-1]


print(lonelyinteger([34, 95, 34, 64, 45, 95, 16, 80, 80, 75, 3, 25, 75, 25, 31, 3, 64, 16, 31]))