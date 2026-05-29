class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d, v = {}, {}
        for l in s:
            d[l] = d.setdefault(l, 1) + 1
        for l in t:
            v[l] = v.setdefault(l, 1) + 1 
        return v == d