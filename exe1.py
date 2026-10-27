def find_largest(numbers):
    large = numbers[0]

    for count in numbers:
        if count > large:
            large = count
    return large
print(find_largest([3, 41, 56, 21, 76, 9]))