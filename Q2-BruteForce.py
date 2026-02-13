# Q2-BruteForce.py
# Aidan Gallagher aidangallagher@sandiego.edu

def max_non_overlapping(intervals):
    best = 0
    n = len(intervals)
    # try every subset
    for mask in range(1 << n):
        subset = []
        for i in range(n):
            if mask & (1 << i):
                subset.append(intervals[i])
        if no_overlap(subset):
            best = max(best, len(subset))
    return best



def no_overlap(subset):
    subset.sort()  # sort by start time
    for i in range(1, len(subset)):
        # overlap if current starts before previous ends
        if subset[i][0] < subset[i - 1][1]:
            return False
    return True



if __name__ == "__main__":
    intervals = [(1, 3), (2, 5), (4, 6), (6, 8), (7, 9)]
    print(max_non_overlapping(intervals))  # Expected: 3
