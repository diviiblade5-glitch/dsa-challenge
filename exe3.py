def  list_sum(numbers):
    if numbers == []:
        return 0
    total = 0

    for number in numbers:
        total = total + number
    return total
print(list_sum([2, 4, 6, 8]))