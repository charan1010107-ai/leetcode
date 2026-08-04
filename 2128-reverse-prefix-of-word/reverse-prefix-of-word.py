class Solution(object):
    def reversePrefix(self, word, ch):
        """
        :type word: str
        :type ch: str
        :rtype: str
        """
        co=0
        if ch not in word:
            return word
        else:
            for i in range(len(word)):
                if word[i]==ch:
                    co=i
                    break
            x=word[:co+1]
            return x[::-1]+word[co+1:]
            
