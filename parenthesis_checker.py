'''
Given an expression string exp. Examine whether the pairs and the orders of “{“,”}”,”(“,”)”,”[“,”]” are correct in exp.
For example, the program should print 'balanced' for exp = “[()]{}{[()()]()}” and 'not balanced' for exp = “[(])”
'''


def check_parenthesis(exp):
    stack = []

    for c in exp:
        if (c == '(') | (c == '{') | (c == '['):
            stack.append(c)
        if c == ')':
            if not stack: return False
            elif stack.pop() != '(': return False
        if c == '}':
            if not stack: return False
            elif stack.pop() != '{': return False
        if c == ']':
            if not stack: return False
            elif stack.pop() != '[': return False
    if not stack:
        return True
    else: return False


def test(exp):
    b = check_parenthesis(exp)
    if b:
        print('Balanced')
    else:
        print('Not balanced')


exp = '(({})[{()}])'
test(exp)   # print balanced

exp = '(({})[{()}])()}'
test(exp)   # print not balanced
