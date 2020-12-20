''' Find the number of correct parenthesis expressions, N
opening and N closing brackets ('(())' - True, '([)]' & ')(()' - False).
N is entered from the keyboard and N is a positive integer. '''


def isValid(s):
    bracket_map = {"(": ")", "[": "]",  "{": "}"}
    open_par = set(["(", "[", "{"])
    stack = []
    for i in s:
        if i in open_par:
            stack.append(i)
        elif stack and i == bracket_map[stack[-1]]:
                stack.pop()
        else:
            return False
    return stack == []


# print(isValid('(()(()))'))    # True
print(isValid('[(])'))    # False