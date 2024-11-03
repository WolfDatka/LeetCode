import time

class Solution(object):
    def findTarget(self, nums, target, excludedI):
        excludeVal = nums[excludedI]

        for i in range(len(nums)):
            if i == excludedI:
                continue

            if nums[i] + excludeVal == target:
                return i

        return False

    def twoSum(self, nums, target):
        for i in range(len(nums)):
            target_val = Solution.findTarget(self, nums, target, i)

            if type(target_val) == int:
                return [i, target_val]

if __name__ == "__main__":
    nums: list = [11, 2, 7, 15, 3, 3]
    target: int = 6

    start = time.time()
    print(Solution.twoSum(Solution, nums, target))
    end = time.time()
    print(end - start)
