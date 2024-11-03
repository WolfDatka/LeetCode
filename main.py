class Solution(object):
    def isValid(self, s):
        if len(s) % 2 != 0:
            return False

        bracket_type_0 = 0
        bracket_type_1 = 0
        bracket_type_2 = 0

        for char in s:
            match char:
                case '(':
                    bracket_type_0 += 1
                case ')':
                    bracket_type_0 -= 1
                case '[':
                    bracket_type_1 += 1
                case ']':
                    bracket_type_1 -= 1
                case '{':
                    bracket_type_2 += 1
                case '}':
                    bracket_type_2 -= 1

            if bracket_type_0 < 0 or bracket_type_1 < 0 or bracket_type_2 < 0:
                return False

        if bracket_type_0 == 0 and bracket_type_1 == bracket_type_0 and bracket_type_2 == bracket_type_0:
            return True

        return False
