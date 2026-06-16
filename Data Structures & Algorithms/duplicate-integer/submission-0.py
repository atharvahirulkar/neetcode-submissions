class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums_droppedDuplicate = set(nums)
        return bool((-len(nums_droppedDuplicate)+len(nums)))