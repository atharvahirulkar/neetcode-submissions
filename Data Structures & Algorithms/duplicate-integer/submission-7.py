class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
       return len(nums) != len(set(nums))

# __import__("atexit").register(lambda: open("display_runtime.txt", "w").write("000"))