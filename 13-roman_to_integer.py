class Solution:
    def romanToInt(self, s: str) -> int:
        # val = 0
        # num = 0
        # for char in s[::-1]:
        #     match char:
        #         case 'I': num = 1
        #         case 'V': num = 5
        #         case 'X': num = 10
        #         case 'L': num = 50
        #         case 'C': num = 100
        #         case 'D': num = 500
        #         case 'M': num = 1000
        #     if 4 * num < val:
        #         val -= num
        #     else:
        #         val += num
        # return val

        val = 0
        prev = ''
        for char in s:
            match char:
                case 'I':
                    val += 1;
                case 'V':
                    if prev == 'I':
                        val += 3
                    else:
                        val += 5
                case 'X':
                    if prev == 'I':
                        val += 8
                    else:
                        val += 10
                case 'L':
                    if prev == 'X':
                        val += 30
                    else:
                        val += 50
                case 'C':
                    if prev == 'X':
                        val += 80
                    else:
                        val += 100
                case 'D':
                    if prev == 'C':
                        val += 300
                    else:
                        val += 500
                case 'M':
                    if prev == 'C':
                        val += 800
                    else:
                        val += 1000
            prev = char
        return val
