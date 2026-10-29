def reverse_first(queue, k):
    queue[:k] = queue[:k][::-1]
    return queue
print(reverse_first([10, 20, 30, 40, 50], k = 3))    