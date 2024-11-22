class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        mp = {}

        for path in paths:
            mp[path[0]] = path[1]

        for i in mp:
            if not mp[i] in mp:
                return mp[i]