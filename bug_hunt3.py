def remove_negatives ( numbers ) :
    non_negative = []
    for num in numbers :
        if num >= 0:
            non_negative.append(num)
    return non_negative

print ( remove_negatives ([1 , -2 , -3 , 4 , -5]) )