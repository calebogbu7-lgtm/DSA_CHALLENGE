def has_duplicates(numbers):
    seen = set()
    for x in numbers:
        if x in seen:
            return True 
        seen.add(x)
    return False

print(has_duplicates([1, 2, 3, 2]))
print(has_duplicates([1, 2, 3, 4]))
print(has_duplicates([]))
  