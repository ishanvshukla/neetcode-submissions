class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # store frequencies in hashmap
        # use min heap to iterate through hashmap and collect top K elements

        freq = {}

        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1

        # build a list of (value, key tuples and heapify) it
        min_heap = []
        for key, val in freq.items():
            cur = [val, key]
            min_heap.append(tuple(cur))
        
        heapq.heapify(min_heap)

        for i in range(len(min_heap) - k):
            print(i)
            heapq.heappop(min_heap)

        result = []
        for i in range(len(min_heap)):
            top = heapq.heappop(min_heap)
            result.append(top[1])
        return result


        