    def valid_paren(s):
        hm = {"(": ")", "[": "]", "{": "}"}
        stk = []
        for c in s:
            if c in hm:
                stk.append(hm[c])
            else:
                if not stk or stk.pop() != c:
                    return False
                
        return len(stk) == 0
