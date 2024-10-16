class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        triangle = [[1]]

        for i in range(1, numRows):
            if i == 1:
                triangle.append([1, 1])
                continue

            newRow = [1]
            prev = triangle[i-1]
            for j in range(len(prev)):
                if j + 1 < len(prev):
                    newRow.append(prev[j] + prev[j + 1])
            newRow.append(1)
            triangle.append(newRow)

        return triangle