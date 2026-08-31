class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        print(len(set(nums)))
        return True if len(set(nums)) != len(nums) else False