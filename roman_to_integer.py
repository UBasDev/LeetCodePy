class RomanToIntegerSolution:
    def roman_to_integer1(self, s: str) -> int:
        total_value:int = 0
        if s == None or len(s) == 0 or s.strip() == '':
            return total_value
        dct = { 'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000 }
        for i in range(len(s)-1):
                current_val = dct[s[i]]
                next_val = dct[s[i+1]]
                total_value += current_val if current_val >= next_val else -current_val
        total_value += dct[s[len(s)-1]]
        return total_value