def find_smallest(numbers):
    if len(numbers) == 0:
        return None
    largest_number = numbers[0]
    for x in numbers:
        if x < largest_number:
            largest_number = x
    return largest_number

print(find_smallest([]))
print(find_smallest([8, 3, 12, 1, 7]))
print(find_smallest([-3, -10, -1, -7]))