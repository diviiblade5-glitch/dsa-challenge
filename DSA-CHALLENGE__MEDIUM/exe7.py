def first_position(numbers, target):
    left = 0
    right = len(numbers) - 1
    answer = -1

    while left <= right:
        middle = (left + right) // 2

        if numbers[middle] == target:
            answer = middle
            right = middle - 1

        elif numbers[middle] < target:
            left = middle + 1

        else:
            right = middle - 1

    return answer
print(first_position([2, 4, 4, 4, 8, 10], target = 4))    