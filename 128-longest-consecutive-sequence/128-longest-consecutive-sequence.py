class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        longest_sequence = 0
        
        for n in nums:
            # check if its the start of a sequence
            if (n - 1) not in num_set:
                length = 0
                while (n + length) in num_set:
                    length += 1
                longest_sequence = max(longest_sequence, length)
        return longest_sequence
                
        