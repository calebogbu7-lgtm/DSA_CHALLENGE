def count_occurrences(numbers, target):
    count = 0
    for x in numbers:
        if x == target:
            count = count + 1
    return count
print(count_occurrences([2, 5, 2, 8, 2], target = 2))
print(count_occurrences([1, 4, 7], target = 10))
