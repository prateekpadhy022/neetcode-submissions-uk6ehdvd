class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        setnum = set(nums)
        lon = 0
        for i in setnum:
            if (i-1) not in setnum:
                leng = 1
                while (i+leng) in setnum:
                    leng += 1
                lon = max(leng,lon)
        
        return lon
            

        
            
        
            