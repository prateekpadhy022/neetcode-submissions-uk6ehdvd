class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        has = {}
        res = []
        for i in nums:
            if i not in has:
                has[i] = 1
            else:
                has[i] += 1
        top_n = dict(sorted(has.items(), key=lambda item: item[1], reverse=True)[:k])
        res = list(top_n.keys())
        return res

