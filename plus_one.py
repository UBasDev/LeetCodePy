class PlusOneSolution:
    def plus_one(self, digits: list[int]) -> list[int]:
        number =  0
        for i in range(len(digits)):
            k = 10**i
            number += digits[-i-1] * k
        
        number = int(number) + 1
        return [int(i) for i in str(number)]
    
    def plus_one2(self, digits: list[int]) -> list[int]:
        return [int(i) for i in str(int(''.join([str(i) for i in digits])) + 1)]