class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        res=sorted(set(nums))
        nums[:len(res)]=res
        return len(res)