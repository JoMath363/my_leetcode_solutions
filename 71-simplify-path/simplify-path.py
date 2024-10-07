class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []

        for s in path.split('/'):
            if s == '.' or s == '':
                continue
            elif s == '..':
                if len(stack):
                    stack.pop()
            else:
                stack.append(s)

        return f"/{'/'.join(stack)}"