class LongestCommonPrefixSolution:
    def longest_common_prefix(self, strs: list[str]) -> str:
        if len(strs) == 1:
            return strs[0]
        strs = sorted(strs)
        shortest_word = strs[0]
        rest_of_word = strs[1:]
        for i in range(len(shortest_word)):
            is_all_matched = True
            for j in range(len(rest_of_word)):
                if shortest_word[:i+1] == rest_of_word[j][:i+1]:
                    continue
                else:
                    is_all_matched = False
                    break
            if not is_all_matched:
                return shortest_word[:i]
        return shortest_word
    
    def longest_common_prefix2(self, strs: list[str]) -> str:
        strs: list[str] = sorted(strs)
        shortest_word = strs[0]
        for i in range(len(shortest_word)):
            if shortest_word[:i+1] != strs[-1][:i+1]:
                return shortest_word[:i]
        return shortest_word