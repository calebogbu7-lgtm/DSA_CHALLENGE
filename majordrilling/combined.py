def list_sum(numbers):
    total = 0
    for x in numbers:
        total += x
    return total
print(list_sum([2, 4, 6, 8]))


def count_occurrences(numbers, target):
    count = 0
    for x in numbers:
        if x == target:
            count = count + 1
    return count

print(count_occurrences([2, 5, 2, 8, 2], target = 2))

def first_occurences(numbers, target):
    for index, value in enumerate(numbers):
        if value  == target:
            return index
print(first_occurences([4, 7, 2, 7, 9], target = 7))


def find_number(numbers, target):
    for x, y in(enumerate(numbers)):
        if y == target:
            return y
    return -1

print(find_number([10, 25, 30, 45], target = 30))

def reverse_list(items):
    result = []
    for x in items:
        result.insert(0, x)
    return result

print(reverse_list([1, 2, 3, 4]))

def reverse_list(items):
    result = []
    for x in items:
        result.insert(0, x)
    return result
print(reverse_list([3, 5, 6, 7]))
print(reverse_list([-1, -0, -8, 9]))

def smallest(numbers):
    if len(numbers) == 0:
        return None
    smallest_number = numbers[0]
    for x in numbers:
        if x < smallest_number:
            smallest_number = x
    return smallest_number

print(smallest([]))
print(smallest([8, 3, 12, 1, 7]))
print(smallest([-3, -10, -1, -7]))

def has_duplicate(numbers):
        duplicate = set()
        for x in numbers:
            if x in duplicate:
                return True
            duplicate.add(x)
        return False

print(has_duplicate([1, 2, 3, 2]))
print(has_duplicate([1, 2, 3, 4]))
print(has_duplicate([]))
print(has_duplicate([5, 5, 5]))

def first_duplicate(numbers):
    duplicate = set()
    for i in numbers:
        if i in duplicate:
            return i
        duplicate.add(i)
    return duplicate


print(first_duplicate([4, 2, 2, 7, 2, 7, 5, 4]))


def move_zero(numbers):
    zero = []
    for x in numbers:
       if x == 0:
           zero = x
       zero.insert(1, x)
    return x
print(move_zero([0, 1, 0, 3, 12]))

    
        
    

