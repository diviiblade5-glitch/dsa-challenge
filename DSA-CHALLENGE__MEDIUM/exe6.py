def closest_number(numbers, target):
    closest = numbers[0]

    for number in numbers:
        if abs(number - target) < abs(closest - target):
            closest = number
        elif abs(number - target) == abs(closest - target) and number < closest:
            closest = number

    return closest
