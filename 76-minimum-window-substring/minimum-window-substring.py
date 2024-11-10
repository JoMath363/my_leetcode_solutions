class Solution:
    def minWindow(self, s: str, t: str) -> str:
        tCount = Counter(t)
        mp = defaultdict(int)
        l, r = 0, 0
        res = None
        required = len(tCount)
        formed = 0

        while r < len(s):
            if s[r] in tCount:
                mp[s[r]] += 1
                if mp[s[r]] == tCount[s[r]]:
                    formed += 1

            while l <= r and formed == required:
                if not res or (r - l + 1) < len(res):
                    res = s[l:r+1]

                if s[l] in tCount:
                    if mp[s[l]] == tCount[s[l]]:
                        formed -= 1
                    mp[s[l]] -= 1
                l += 1

            r += 1

        return res if res else ""



        


