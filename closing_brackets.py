
def is_matching_brackets(s):
    stack = []
    mapping = {')': '(', '}': '{', ']': '['}
    for char in s:
        if char in mapping:
            if not stack or stack.pop() != mapping[char]:
                return False
        else:
            stack.append(char)
    return not stack


def is_matched(expression):
    stack = []
    opening = set(['(', '[', '{'])
    closing = set([')', ']', '}'])
    mapping = {')': '(', ']': '[', '}': '{'}
    for char in expression:
        if char in opening:
            stack.append(char)
        elif char in closing:
            if not stack:
                return False
            elif stack[-1] == mapping[char]:
                stack.pop()
            else:
                return False
    return not stack
