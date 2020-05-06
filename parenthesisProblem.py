def isBalanced(s):
    stack = []
    for char in s:
        if char in ['[','{','(']:
            stack.append(char)
        else:
            if not stack:
                return False
            current_char = stack.pop()
            if char == ')':
                if current_char != '(':
                    return False
            if char == '}':
                if current_char != '{':
                    return False
            if char == ']':
                if current_char != '[':
                    return False
    if len(stack) == 0:
        return True
    else:
        return False
                
               
s = '[()]{}{[()()]()}'
#s = ']'
#s = '(])'
#s = ''
#s = '[])'

print(isBalanced(s))