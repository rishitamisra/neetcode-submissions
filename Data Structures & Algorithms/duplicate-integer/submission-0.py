class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        a=[]
        for items in nums:
            if items not in a:
                a.append(items)
            else:
                return True
        return False