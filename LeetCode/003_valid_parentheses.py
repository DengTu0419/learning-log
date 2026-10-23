class Solution(object):
    def isValid(self, s):
        pars = {")":"(","]":"[","}":"{"}
        stack = []
        for ch in s:
            if ch in "({[":
                stack.append(ch)
            else:
                if not stack:
                    return False
                if stack.pop() != pars[ch]:
                    return False
        return not stack
