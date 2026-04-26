class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        checked_nums = {} # value : index

        for idx, n in enumerate(nums):
            new_target = target - n
            if new_target in checked_nums:
                return [checked_nums[new_target], idx]
            checked_nums[n] = idx
            


