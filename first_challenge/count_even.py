def count_even(numbers):
    count = 0
    for x in (range(len(numbers))):
        if x % 2 == 0:
            count = count + 1
    return count
print(count_even([1, 2, 3, 4, 6]))
