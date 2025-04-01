import math

class JumpSearchAndBinarySearchSolution:
    def jump_search(self, arr, target) -> int:
        
        length_of_arr: int = len(arr)
        
        if length_of_arr == 0:
            return -1
        
        elif length_of_arr == 1:
            return 0 if arr[0] == target else -1
        
        elif target < arr[0] or target > arr[-1]:
            return -1
        
        increase: int = int(math.sqrt(length_of_arr))
        
        current_step: int = increase
        
        prev_step: int = 0
        
        while current_step < length_of_arr and arr[current_step] <= target:
            
            prev_step = current_step
            
            current_step += increase
        
        return self.__binary_search(arr, target, prev_step, min(current_step, length_of_arr - 1))
    
    def __binary_search(self, arr, target, prev_step, current_step) -> int:
        
        left_idx: int = prev_step
        
        right_idx: int = current_step
        
        while left_idx <= right_idx:
            
            mid_idx: int = (right_idx+left_idx) // 2
            
            if arr[mid_idx] == target:
                return mid_idx
            elif arr[mid_idx] < target:
                left_idx = mid_idx + 1
            else:
                right_idx = mid_idx -1
            
        return -1