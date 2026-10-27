class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # [1,2,4,6] -> [1, 1, 2, 8]
        # [1,2,4,6] -> [, 6, 1]
        # we can multiply the prefix and postfix products to see what the product is
        # without nums[i]
        # the prefix array will carry the products of all the elements before nums[i]
        # and the postfix array will carry the products of all the elements after nums[i]
        # so effectively, when you multiply these together, it'll multiply all the elements together
        # except what was at the current index
        length = len(nums)
        prefix = [0] * length
        # populate prefix array
        prefix[0] = 1
        prefix_product = 1
        for i in range(1, length):
            prefix_product *= nums[i - 1]
            prefix[i] = prefix_product

        # populate postfix array
        postfix_product = 1
        for j in range(length - 2, -1, -1):
            postfix_product *= nums[j + 1]
            prefix[j] = postfix_product * prefix[j]
            
        return prefix

'''
Time Complexity: O(n) -> takes n steps to build prefix array, n for postfix and n for result so n + n + n = 3n which simplifies to O(n) because you drop constant factors
Space Complexity: O(n) -> prefix and postfix arrays are of length n
'''