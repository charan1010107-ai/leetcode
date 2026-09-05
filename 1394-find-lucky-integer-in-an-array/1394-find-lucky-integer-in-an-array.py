class Solution(object):
    def findLucky(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        li=[]
        for i in range(len(arr)):
            if arr.count(arr[i])==arr[i]:
                li.append(arr[i])
        if li:
            return max(li)
        else:
            return -1