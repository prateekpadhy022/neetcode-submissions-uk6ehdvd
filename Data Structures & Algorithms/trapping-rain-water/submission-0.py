class Solution:
    def trap(self, h: List[int]) -> int:
        c = 0
        l = 0
        r = len(h) - 1
        lm = h[l]
        rm = h[r]
        res = 0
        while l < r:
            if lm < rm:
                l += 1
                lm = max(h[l],lm)
                res += lm - h[l]
            else:
                r -= 1
                rm = max(h[r],rm)
                res += rm - h[r]

        return res


            