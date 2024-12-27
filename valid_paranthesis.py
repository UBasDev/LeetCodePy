class ValidParanthesisSolution:
    def is_valid(self, s: str) -> bool:
        if len(s)&2 == 1:
            return False
        my_dict: dict[str, str] = {
            '(': ')',
            '{': '}',
            '[': ']',
        }
        my_stack: list[str] = []
        
        for my_char in s:
            if my_char in my_dict.keys():
                my_stack.append(my_char)
            elif my_char in my_dict.values():
                if not my_stack or my_dict[my_stack.pop()] != my_char:
                    return False
        return len(my_stack) == 0