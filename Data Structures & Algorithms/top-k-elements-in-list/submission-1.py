class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1

        min_heap = []
        for num, count in freq.items():
            min_heap.append((count, num))
        heapq.heapify(min_heap)

        while len(min_heap) > k:
            heapq.heappop(min_heap)

        result = []
        for count, num in min_heap:
            result.append(num)
        return result