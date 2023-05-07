# Given a string s containing just the characters
# '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# 1. Open brackets must be closed by the same type of brackets.
# 2. Open brackets must be closed in the correct order.
# 3. Every close bracket has a corresponding open bracket of the same type.

class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {')': '(', '}': '{', ']': '['}
        stack = []
        for b in s: 
            if b in brackets: # If b is a closing brace.
                # If there's nothing to compare or if the brackets don't match.
                if not stack or stack.pop() != brackets[b]:
                    return False
            else:
                stack.append(b)

        return len(stack) == 0

s = Solution()

assert s.isValid('()') is True
assert s.isValid('[()[]]') is True
assert s.isValid('[(])') is False

print ('ALL TESTS PASS')
