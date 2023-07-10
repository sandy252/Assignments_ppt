def merge_intervals(intervals):
    intervals.sort(key=lambda x: x[0])  # Sort intervals based on start times
    merged = []

    for interval in intervals:
        if not merged or interval[0] > merged[-1][1]:
            merged.append(interval)
        else:
            merged[-1][1] = max(merged[-1][1], interval[1])

    return merged
