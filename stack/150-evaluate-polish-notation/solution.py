class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if not tokens:
            return 0
        
        stk = []
        
        for c in tokens:
            if c in ["+", "-", "*", "/"]:
                bottom, top = stk.pop(), stk.pop()
                if c == "+":
                    stk.append(top + bottom)
                elif c == "-":
                    stk.append(top - bottom)
                elif c == "*":
                    stk.append(top * bottom)
                elif c == "/":
                    stk.append(int(top / bottom))
            else:
                stk.append(int(c))

                
        return stk[-1]