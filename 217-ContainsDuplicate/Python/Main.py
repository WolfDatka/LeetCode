import time

def containsDuplicate(nums):
    nums.sort()

    for i in range(1, len(nums)):
        if nums[i - 1] == nums[i]:
            return True

    return False

if __name__ == "__main__":
    nums: list = []

    with open("./../NegativeContainsDuplicateNumsList.txt", 'r') as f:
        read_count = 0
        print(f"{read_count} lines read", end='')

        for line in f:
            nums.append(int(line))
            read_count += 1
            print(f"\r{read_count} lines read", end='')

        print()
        f.close()

    start = time.time()
    print(containsDuplicate(nums))
    end = time.time()
    print(f"{end - start}s")
