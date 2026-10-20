class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # hashmap will store (element, index) pairs
        seenNums = {}

        # go through list and see if target - current num is in the hashmap, then we have found our match
        for i in range(len(nums)):
            cur = nums[i]
            diff = target - cur
            if diff in seenNums:  
                return [seenNums[diff], i]
            else:
                seenNums[cur] = i

        return []

        