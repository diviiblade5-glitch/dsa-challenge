def has_duplicates(numbers):
    seen = set()

    for number in numbers:
        if number in seen:
            return True

        seen.add(number)

    return False
print(has_duplicates([1, 2, 3, 4]))    