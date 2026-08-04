class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        res=[]
        minv=min(nums)
        maxv=max(nums)
        for i in range(minv+1,maxv):
            if i not in nums:
                res.append(i)
        return res