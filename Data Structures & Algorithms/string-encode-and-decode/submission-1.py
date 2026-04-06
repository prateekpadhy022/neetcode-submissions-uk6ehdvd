class Solution:

    def encode(self, strs: List[str]) -> str:
        # de = ""
        # for i in strs:
        #     de = de+i+str(1)
        # print(de)
        # return de
        de = ""
        for i in strs:
            de += str(len(i))+"#"+i
        print(de)
        return de
        
    def decode(self, s: str) -> List[str]:
        en = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            i = j + 1
            j = i + length
            en.append(s[i:j])
            i = j
        return en