class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for c in s:
            if c in "([{":
                stack.append(c)
                continue

            if not stack:
                return False

            popped = stack.pop()
            if c == ")" and popped != "(":
                return False
            elif c == "]" and popped != "[":
                return False
            elif c == "}" and popped != "{":
                return False

        return len(stack) == 0
