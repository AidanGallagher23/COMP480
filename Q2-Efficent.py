# Efficient 
# Aidan Gallagher aidangallagher@sandiego.edu

def max_non_overlapping(intervals):
    # If there are no intervals
    if len(intervals) == 0:
        return 0
    # Sort intervals by their end time (smallest end first)
    intervals = sorted(intervals, key=lambda interval: interval[1])
    count = 0
    current_end = 0
    for interval in intervals:
        start = interval[0]
        end = interval[1]
        # If this interval does not overlap with the last chosen one
        if start >= current_end:
            count += 1
            current_end = end
    return count


# Example
if __name__ == "__main__":
    intervals = [(1, 3), (2, 5), (4, 6), (6, 8), (7, 9)]
    result = max_non_overlapping(intervals)
    print("Maximum number of non-overlapping intervals:", result)