class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        ham = set(nums)
        if len(ham) == len(nums):
            return False
        else:
            return True