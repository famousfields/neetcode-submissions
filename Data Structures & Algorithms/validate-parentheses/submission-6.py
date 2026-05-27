class Solution:
    def isValid(self, s: str) -> bool:
        stk = []

        for i in s:
            if i == "(" or i == "[" or i == "{":
                stk.append(i)
            else:
                if stk:
                    top = stk[-1]
                    if i == ")" and top != "(":
                        return False
                    elif i == "]" and top != "[":
                        return False
                    elif i == "}" and top != "{":
                        return False
                    stk.pop()
                else:
                    return False
        return True if len(stk) == 0 else False
        