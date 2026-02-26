import math


def main():

    nums = list(map(int, input("Enter Array: ").split()))
    print("Max Sum Sum Array: ", peakElement(nums))


def peakElement(nums):
    start = 0
    end = len(nums) - 1

    while start != end:
        middle = (start + end) // 2
        if nums[middle] > nums[middle + 1]:
            # going down, so peak to left
            end = middle
        else:
            # going up, so peak to right
            start = middle + 1

    return start


if __name__ == "__main__":
    main()
