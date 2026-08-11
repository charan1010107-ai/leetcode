class Solution(object):
    def earliestTime(self, tasks):
        """
        :type tasks: List[List[int]]
        :rtype: int
        """
        x=[]
        for i in range(len(tasks)):
            s=sum(tasks[i])
            x.append(s)
            res=min(x)
        return res