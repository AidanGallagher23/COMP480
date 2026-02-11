import math


def main():
    nums = list(
        map(int, input("Enter Array seperated by space (i.e: 1 6 2 3 6): ").split())
    )
    print("Max Sum Sum Array: ", maxSubArrayBruteForce(nums))


def maxSubArrayBruteForce(nums):
    ans = -math.inf
    for i in range(len(nums)):
        cur_sum = 0
        for j in range(i, len(nums)):
            cur_sum += nums[j]
            ans = max(ans, cur_sum)
    return ans


if __name__ == "__main__":
    main()
