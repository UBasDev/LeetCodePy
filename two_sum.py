class TwoSumSolution:
    def two_sum1(self, nums: list[int], target: int) -> list[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []
    def two_sum2(self, nums: list[int], target: int) -> list[int]:
        for i in range(len(nums)):
            extracted = target - nums[i]
            rest_of_list = nums[i+1:]
            if extracted in rest_of_list:
                return [i, rest_of_list.index(extracted) + (len(nums) - len(rest_of_list))]
        return []