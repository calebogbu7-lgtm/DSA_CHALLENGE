def list_sum(numbers):
    total = 0
    for x in numbers:
        total += x
    return total

print(list_sum([]))
print(list_sum([2, 4, 6, 8]))
print(list_sum([-5, 10, -2]))


