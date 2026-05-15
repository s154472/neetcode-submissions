class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sum_dict = {}
        current = nums[0]
        for i in range(len(nums)):
            if target - nums[i] in sum_dict:
                return [sum_dict[target - nums[i]], i]
            else:
                sum_dict[nums[i]] = i
