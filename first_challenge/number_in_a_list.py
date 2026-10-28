def find_number(number, target):
    for x in range(len(number)): 
        if number[x] == target:
            return x
    return -1

print(find_number([10, 25, 30, 45], target = 30))
print(find_number([5, 8, 5, 9], target = 5))
print(find_number([10, 20, 30], target = 99))
     