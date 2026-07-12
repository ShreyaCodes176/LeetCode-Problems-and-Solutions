class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n=len(nums)
        nMap={}
        for i in range(n):
            complement=target-nums[i]
            if complement in nMap:
                return [nMap[complement],i] #return as list the index of complement and i
            nMap[nums[i]]=i #adding the complement to the map
            
        return [] #no solution