class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from string import ascii_lowercase as alphabet
        def to_dict(x):
            d = {_:0 for _ in alphabet}
            for l in x: d[l] += 1
            return ''.join([i+str(j) for i,j in d.items()])

        r = {}
        for s in strs:
            d = to_dict(s)
            r.setdefault(d, []).append(s)
        return list(r.values())
