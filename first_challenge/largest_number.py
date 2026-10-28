def find_largest(numbers):
    if len(numbers) == 0:
        return None
    largest_number = numbers[0]
    for x in numbers:
        if x > largest_number:
            largest_number = x
    return largest_number
print(find_largest([]))
print(find_largest([3, 41, 56, 21, 76, 9]))
print(find_largest([-10, -5, -2, -18]))