def find_number(numbers, target):
    for index in range(len(numbers)):
        if numbers[index] == target:
            return index

    return -1
print(find_number(numbers = [10, 25, 30, 45], target = 30))    