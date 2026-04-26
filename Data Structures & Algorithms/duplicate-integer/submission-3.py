class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        len_nums = len(nums)
        nums_unique = set(nums)
        len_set = len(nums_unique)
        if len_nums == len_set:
            return False
        else:
            return True
        