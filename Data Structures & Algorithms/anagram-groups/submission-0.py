class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for i in strs:
            check = ''.join(sorted(i))
            res[check].append(i)
        return list(res.values())

        