def merge_intervals(intervals):
    intervals.sort()

    merged = [intervals[0]]

    for interval in intervals[1:]:
        current = merged[-1]

        if interval[0] <= current[1]:
            current[1] = max(current[1], interval[1])
        else:
            merged.append(interval)

    return merged
intervals = [[1, 3], [2, 6], [8, 10], [9, 12]]

print(merge_intervals(intervals))