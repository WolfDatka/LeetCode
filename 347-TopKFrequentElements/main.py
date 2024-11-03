from collections import Counter
from heapq import heappush, heappop

class Solution(object):
    def topKFrequent(nums, k):
        num_frequencies = Counter(nums)
        min_heap = []

        for num, freq in num_frequencies.items():
            heappush(min_heap, (freq, num))
            if len(min_heap) > k:
                heappop(min_heap)

        top_k_frequent = [pair[1] for pair in min_heap]

        print(top_k_frequent)

if __name__ == "__main__":
    nums = [4,1,-1,2,-1,2,3]
    k = 2
    print(Solution.topKFrequent(nums, k))
