class Solution:
    def isPalindrome(self, s: str) -> bool:
        si = ''.join(e for e in s if e.isalnum()).lower()
        print(si)
        sir = si[::-1]
        if si == sir:
            return True
        else:
            return False
