import heapq

def min_classrooms(intervals):
    # sort intervals by start time
    intervals.sort(key=lambda x: x[0])

    # min heap to track earliest ending lecture
    heap = []

    for start, end in intervals:
        if heap and heap[0] <= start:
            heapq.heappop(heap)

        heapq.heappush(heap, end)

    return len(heap)


# Example
intervals = [[30,75],[0,50],[60,150],[80,120],[55,65]]
print(min_classrooms(intervals))

#test cases
test1 = [[1,2], [3,4], [5,6]] # no overlap, return 1
test2 = [[1,4], [2,5], [7,9]] # 1 overlap, return 2
test3 =[[1,10], [2,9], [3,8], [4,7]] # everything overlaps, return 4
print("test1: " + str(min_classrooms(test1)) + " expected: 1")
print("test2: " + str(min_classrooms(test2)) + " expected: 2")
print("test3: " + str(min_classrooms(test3)) + " expected: 4")