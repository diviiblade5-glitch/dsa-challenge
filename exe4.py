def count_even(numbers):
    cleaned = 0

    for count in numbers:
        if count % 2 == 0:
            cleaned += 1
    return cleaned 
print(count_even([1, 3, 5, 7]))    