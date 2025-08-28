class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if not a:
            return b
        if not b:
            return a
        
        i, j = len(a) - 1, len(b) - 1
        carry = 0
        res = []

        while i >= 0 or j >= 0 or carry:
            n = 0 if i < 0 else int(a[i])
            m = 0 if j < 0 else int(b[j])

            digit = (carry + n + m) % 2
            carry = (carry + n + m) // 2
            i -= 1
            j -= 1
            res.append(str(digit))

        return "".join(res[::-1])
