class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        longest = 0
        for num in nums:
            if num-1 not in numset:
                curr = num
                l = 1
                while curr + 1 in numset:
                    curr += 1
                    l += 1
                
                longest = max(longest, l)


        return longest