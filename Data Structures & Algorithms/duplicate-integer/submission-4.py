class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        original = len(nums)
        deduped = len(set(nums))
        if original != deduped:
            return True
        else:
            return False