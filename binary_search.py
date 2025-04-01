class BinarySearchSolution:
    def binary_search(self, item_list: list[int], searched_item: int):
        left: int = 0
        
        right: int = len(item_list)-1
        
        while left <= right:
            mid_index = (left + right) // 2
            
            if item_list[mid_index] == searched_item:
                return mid_index
            elif item_list[mid_index] < searched_item:
                left = mid_index + 1
            else:
                right = mid_index - 1
        
        return -1