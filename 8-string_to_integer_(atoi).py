class Solution:
    def myAtoi(self, s: str) -> int:
        sign = 1
        char_set = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        val = ''
        sign_chosen = False
        signs = ['-', '+']
        number_started = False
        for ch in s:
            if sign_chosen and ch in signs: break
            if not number_started and ch == ' ' and not sign_chosen: continue
            if not number_started and ch == '+':
                sign_chosen = True
                continue
            if not number_started and ch == '-':
                sign_chosen = True 
                sign *= -1
                continue
            if ch not in char_set: break
            val += ch
            number_started = True
        if val == '': return 0
        val = int(val) * sign
        if val < -1 * pow(2,31): return -1 * pow(2,31)
        if val > pow(2,31) - 1: return pow(2,31) - 1
        return val
        
            
            
            
