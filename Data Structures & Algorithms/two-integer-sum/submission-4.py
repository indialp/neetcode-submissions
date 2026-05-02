class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        table = {}
        for idx, num in enumerate(nums):
            new_target = target - num
            if new_target in table.keys():
                return sorted([idx, table[new_target]])
            table[num] = idx

        
        