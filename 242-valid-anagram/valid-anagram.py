class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(sorted(s)) == Counter(sorted(t))