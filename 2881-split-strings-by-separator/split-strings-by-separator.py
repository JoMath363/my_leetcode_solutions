class Solution:
    def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:
        res = []

        for w in words:
            res = res + w.split(separator)

        return [x for x in res if not x  == '']