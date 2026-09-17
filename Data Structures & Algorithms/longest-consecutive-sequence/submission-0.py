class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)          # store all numbers for O(1) lookup
        longest = 0                  # track longest sequence length

        for num in num_set:
            if num - 1 not in num_set:   # start only if num is sequence start
                current = num
                length = 1

                while current + 1 in num_set:  # extend the sequence
                    current += 1
                    length += 1

                longest = max(longest, length) # update max length

        return longest