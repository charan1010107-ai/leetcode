class Solution(object):
    def checkIfPangram(self, sentence):
        """
        :type sentence: str
        :rtype: bool
        """
        count=0
        x="abcdefghijklmnopqrstuvwxyz"
        if len(sentence)<26:
            return False
        for i in range(len(x)):
            ch=x[i]
            if ch not in sentence:
                count+=1
        if count==0:
            return True
        else:
            return False