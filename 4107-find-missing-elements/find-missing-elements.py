class Solution(object):
    def findMissingElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        x=sorted(nums)
        res=[]
        z=min(x)
        y=max(x)
        for i in range(z,y+1):
            if i not in nums:
                res.append(i)
        return res