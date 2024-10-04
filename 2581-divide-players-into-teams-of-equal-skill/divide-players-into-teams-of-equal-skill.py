class Solution(object):
    def dividePlayers(self, skill):
        """
        :type skill: List[int]
        :rtype: int
        """
        skill.sort()

        res = 0
        i = 0
        j = len(skill) - 1
        teamVal = skill[0] + skill[j]
        

        while i < j:
            if skill[i] + skill[j] == teamVal:
                res += skill[i] * skill[j]
                i += 1
                j -= 1
            else:
                return -1
        return res
            

        

