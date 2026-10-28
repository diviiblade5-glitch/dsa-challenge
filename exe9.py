def first_duplicate(numbers):
    seen = []

    for first_number in numbers:
        if first_number in seen:
            return first_number

        seen.append(first_number)
    else:    
        return None
print(first_duplicate([4, 7, 2, 7, 5, 4]))    
print(first_duplicate([1, 2, 3, 4]))    
print(first_duplicate( [5, 5, 3]))    