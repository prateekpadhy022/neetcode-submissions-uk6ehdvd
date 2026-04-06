class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # if len(s) == len(t):
        #     for i,x in enumerate(s):
        #         if x in t:
        #             s.replace(s[i],'')
        #             t.replace(t[i],'')
        #             continue
        #         else:
        #             return False
        #     return True
        # else:
        #     return False
        if sorted(s) == sorted(t):
            return True 
        else:
            return False
