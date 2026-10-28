def reverse_list(items):
    result = []
    for x in items:
        result.insert(0, x)
    return result
print(reverse_list([1, 2, 3, 4]))