class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        # letters_s = {}
        # for c in s:
        #     if c in letters_s:
        #         letters_s[c] += 1
        #     else:
        #         letters_s[c] = 1

        # letters_t = {}
        # for c in t:
        #     if c in letters_t:
        #         letters_t[c] += 1
        #     else:
        #         letters_t[c] = 1

        # if letters_s == letters_t:
        #     return True
        # else:
        #     return False
        sorted_s = "".join(sorted(s))
        sorted_t = "".join(sorted(t))

        if sorted_s == sorted_t:
            return True
        else:
            return False