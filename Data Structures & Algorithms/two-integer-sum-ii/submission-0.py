class Solution:
    def twoSum(self, li: List[int], target: int) -> List[int]:
        l = 0
        r = len(li) - 1
        while l < r:
            if (li[l]+li[r] > target):
                r -= 1
            elif(li[l]+li[r] < target):
                l += 1
            else:
                return [l+1,r+1]