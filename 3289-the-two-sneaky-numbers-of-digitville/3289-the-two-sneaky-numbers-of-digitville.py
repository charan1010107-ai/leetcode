class Solution(object):
    def getSneakyNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        x=[]
        for i in range(len(nums)-1,-1,-1):
            y=nums.pop(i)
            if y in nums:
                 x.append(y)
        return x