class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1

        min_heap = []
        heapq.heapify(min_heap)
        for num, count in freq.items():
            if len(min_heap) < k:
                heapq.heappush(min_heap, (count, num))
            elif count > min_heap[0][0]:
                heapq.heappop(min_heap)
                heapq.heappush(min_heap, (count, num))
        

        while len(min_heap) > k:
            heapq.heappop(min_heap)

        result = []
        for count, num in min_heap:
            result.append(num)
        return result