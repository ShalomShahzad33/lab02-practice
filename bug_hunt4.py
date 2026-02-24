def sum_evens ( numbers ) :
    total = 0
    for i in range (len ( numbers ) ) :
        if numbers[i] % 2 == 0:
            total += numbers [ i ]
    return total

print ( sum_evens ([1 , 2 , 3 , 4 , 5 , 6]) )
