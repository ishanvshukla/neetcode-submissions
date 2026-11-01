class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # if the current element - 1 isn't in the array, we know this can be the start of our sequence
        # as long as the next elements from the array are in our set, we can increment our current 
        # sequence that we are tracking by 1
        # after processing the element, check if we have formed the new longest consecutive sequence
        if nums == None or len(nums) == 0:
            return 0
        nums_set = set(nums)
        lcs = 1
        for num in nums_set:
            if num - 1 not in nums_set:
                next_element = num + 1
                current_sequence = 1
                while next_element in nums_set:
                    next_element += 1
                    current_sequence += 1
                lcs = max(lcs, current_sequence)
        return lcs

        