# Leetcode 67. Add Binary
# https://leetcode.com/problems/add-binary/
# Difficulty: Easy
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        def helper(a, b, carry):
            if not a and not b:
                return '1' if carry else ''
            if not a:
                return helper(b, a, carry)
            if not b:
                if carry:
                    if a[-1] == '1':
                        return helper(a[:-1], b, True) + '0'
                    else:
                        return helper(a[:-1], b, False) + '1'
                else:
                    return a
            if a[-1] == '1' and b[-1] == '1':
                if carry:
                    return helper(a[:-1], b[:-1], True) + '1'
                else:
                    return helper(a[:-1], b[:-1], True) + '0'
            elif a[-1] == '1' or b[-1] == '1':
                if carry:
                    return helper(a[:-1], b[:-1], True) + '0'
                else:
                    return helper(a[:-1], b[:-1], False) + '1'
            else:
                if carry:
                    return helper(a[:-1], b[:-1], False) + '1'
                else:
                    return helper(a[:-1], b[:-1], False) + '0'
        return helper(a, b, False)