class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        for i in s:
            if i in t:
                pass
            else:
                return False
        return True