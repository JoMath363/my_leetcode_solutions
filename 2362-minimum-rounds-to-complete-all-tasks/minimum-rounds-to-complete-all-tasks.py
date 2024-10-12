class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        taskmap = {}
        count = 0

        for i in tasks:
            if i in taskmap:
                taskmap[i] += 1
            else:
                taskmap[i] = 1

        for key in taskmap:
            if taskmap[key] == 1:
                return -1
            count += ceil(taskmap[key] / 3)
        return count