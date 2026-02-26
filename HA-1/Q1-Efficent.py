import math


def main():
    nums = list(
        map(int, input("Enter Array seperated by space (i.e: 1 6 2 3 6): ").split())
    )
    print("Max Sum Sum Array: ", maxSubArrayEfficent(nums))


def maxSubArrayEfficent(nums):
    cur_max, max_so_far = -math.inf, -math.inf
    for c in nums:
        cur_max = max(c, cur_max + c)
        max_so_far = max(max_so_far, cur_max)
    return max_so_far


if __name__ == "__main__":
    main()
