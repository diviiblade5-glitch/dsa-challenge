def find_smallest(numbers):
    small = numbers[0]

    for count in numbers:
        if count < small:
            small = count
    return small
print(find_smallest([-3, -10, -1, -6]))