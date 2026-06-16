class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = {}

        for s in strs:
            key = tuple(sorted(s))
            seen[key] = seen.get(key, []) + [s]


        return list(seen.values())