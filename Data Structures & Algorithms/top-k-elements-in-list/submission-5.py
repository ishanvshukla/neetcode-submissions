class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        # count frequencies of every element
        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1

        # store the top k count, element pairs in a min heap
        min_heap = []
        for num, count in freq.items():
            # heap hasn't reached size k
            if len(min_heap) < k:
                heapq.heappush(min_heap, (count, num))
            # current element's count is greater than the one on top of the heap
            elif count > min_heap[0][0]:
                heapq.heappop(min_heap)
                heapq.heappush(min_heap, (count, num))

        # extract the top k elements from the heap
        result = []
        for count, num in min_heap:
            result.append(num)
        return result