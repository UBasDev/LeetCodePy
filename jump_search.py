import math

class JumpSearchSolution:
    
    def jump_search(self, arr: list[int], target: int) -> int:
        
        length_of_arr:int = len(arr)
        
        if length_of_arr == 0:
            return -1
        
        elif length_of_arr == 1:
            return 0 if arr[0] == target else -1
        
        elif target < arr[0] or target > arr[-1]:
            return -1

        increase = int(math.sqrt(length_of_arr))

        current_step = increase
        
        prev_step = 0
        
        while current_step < length_of_arr and arr[current_step] <= target:
            prev_step = current_step
            
            current_step += increase
            
            if prev_step >= length_of_arr:
                return -1
            
        for idx in range(prev_step, current_step):
            if arr[idx] == target:
                return idx
        
        return -1
    
x1 = JumpSearchSolution()

arr1 = [10, 20, 30, 40, 50]

target = 60

x1.jump_search(arr1, target)