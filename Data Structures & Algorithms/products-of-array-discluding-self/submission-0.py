class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        output = [1] * n          # initialize output with 1s

        # Step 1: prefix products
        prefix = 1
        for i in range(n):
            output[i] = prefix    # product of elements to the left
            prefix *= nums[i]     # update prefix product

        # Step 2: suffix products
        suffix = 1
        for i in range(n - 1, -1, -1):
            output[i] *= suffix   # multiply left and right products
            suffix *= nums[i]     # update suffix product

        return output