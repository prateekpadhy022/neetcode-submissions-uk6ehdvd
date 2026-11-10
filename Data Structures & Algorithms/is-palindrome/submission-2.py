class Solution:
    def isPalindrome(self, s: str) -> bool:
        import re
        clean = re.sub(r'[^a-zA-Z0-9]', '', s)
        clean = clean.lower()
        print(clean)
        l, r  = 0, len(clean) - 1
        while l < r:
            if clean[l] == clean[r]:
                l += 1
                r -= 1
            else:
                return False
        return True

        
            