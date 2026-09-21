class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        unique = list(set(nums))
        d = {}

        for n in unique:
            d[n] = 0
        
        for x in nums:
            if x in d:
                d[x] = d[x] + 1

        for v in list(d.values()):
            if v > 1:
                return True
            
        return False

