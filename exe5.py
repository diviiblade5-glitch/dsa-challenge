def count_occurrences(numbers, target):
    counter = 0

    for count in numbers:
        if count == target:
            counter + 1
        return counter
print(count_occurrences([1, 4, 7], target = 10))
