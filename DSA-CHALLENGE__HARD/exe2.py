def longest_consecutive(numbers):
    nums = set(numbers)
    longest = 0

    for number in nums:
        if number - 1 not in nums:
            count = 1

            while number + count in nums:
                count += 1

            longest = max(longest, count)

    return longest
print(longest_consecutive([100, 4, 200, 1, 3, 2]))    