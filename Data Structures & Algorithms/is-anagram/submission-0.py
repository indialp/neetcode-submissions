class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        split_s = list(s)
        split_t = list(t)
        
        split_s.sort()
        split_t.sort()

        new_s = "".join(split_s)
        new_t = "".join(split_t)

        if new_s == new_t:
            return True
        else:
            return False