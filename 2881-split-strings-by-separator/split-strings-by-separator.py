class Solution:
    def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:
        array = []
        for word in words:
            parts = word.split(separator)
            for part in parts:
                if part != '':
                    array.append(part)
        return array