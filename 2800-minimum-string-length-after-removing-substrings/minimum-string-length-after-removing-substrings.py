class Solution:
    def minLength(self, s: str) -> int:
            while "AB" in s or "CD" in s:
                ab = s.find("AB")
                cd = s.find("CD")

                if not ab == -1:
                    s = s[:ab] + s[ab+2:]
                elif not cd == -1:
                    s = s[:cd] + s[cd+2:]

            return len(s)

            