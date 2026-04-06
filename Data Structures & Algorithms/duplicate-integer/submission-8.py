class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        # for i in nums:
        #     arr = i
        #     f = 0
        #     for j in nums:
        #         if arr == j:
        #             f = f+1
        #     if f >=2:
        #         return True
        # return False

        return len(set(nums)) < len(nums)
