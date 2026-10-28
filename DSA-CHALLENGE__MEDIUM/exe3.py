def balanced_brackets(text):
    stack = []
    brackets = {'(': ')', '{': '}', '[': ']'}
    
    for char in text:
        if char in brackets:
            stack.append(char)
        elif char in brackets.values():
            if not stack or brackets[stack.pop()] != char:
                return False
    
    return len(stack) == 0
print (balanced_brackets("(hello)"))    