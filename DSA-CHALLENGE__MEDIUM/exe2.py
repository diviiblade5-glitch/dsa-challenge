def move_zeros(numbers):
    result = []
    zero = 0

    for number in numbers:
        if number == 0:
            zero += 1
        else:
            result.append(number)

    result.extend([0] * zero)

    return result
print(move_zeros([0, 1, 0, 3, 12])) 
print(move_zeros([4, 0, 5, 0, 2])) 
print(move_zeros([1, 2, 3, 4]))