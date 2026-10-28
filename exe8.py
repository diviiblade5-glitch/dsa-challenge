def has_duplicates(numbers):
    seen = []

    for number in numbers:
        if number in seen:
            return True

        seen.append(number)
    else:
        return False

print(has_duplicates([1, 2, 3, 2]))    
print(has_duplicates([1, 2, 3, 4]))    
print(has_duplicates([]))