class PalindromeNumberSolution:
    def is_palindrome1(self, x: int) -> bool:
        return str(x) == str(x)[::-1]
    
    def is_palindrome2(self, x: int) -> bool:
        if x < 0:
            return False
        value_abs = str(x)
        for i in range(len(value_abs)):
            from_start:str = value_abs[i]
            from_bottom:str = value_abs[len(value_abs) -1 -i]
            if from_start != from_bottom:
                return False
        return True