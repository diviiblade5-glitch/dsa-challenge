def two_sum(numbers, target):
    seen = {}

    for i, number in enumerate(numbers):
        needed = target - number

        if needed in seen:
            return [seen[needed], i]

        seen[number] = i

    return None
print(two_sum([2, 7, 11, 15], target = 9))    