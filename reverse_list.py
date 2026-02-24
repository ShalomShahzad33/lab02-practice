def reverse_list(items):
    for i in range(len(items) // 2):
        j = len(items) - 1 - i
        items[i], items[j] = items[j], items[i]
    return items

print(reverse_list([1,2,3,4]))
