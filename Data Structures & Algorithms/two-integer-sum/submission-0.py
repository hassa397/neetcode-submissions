class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #Stores differences
        d = {}

        #Check if difference in dictonary
        for i,n in enumerate(nums):
            if (target - n) in d:
                return [d[target-n],i]
            #If doesn't exit then add to dictionary
            else:
                d[n] = i


        