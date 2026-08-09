class Solution(object):
    def sortVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        res="" 
        caps=""
        sms=""
        n=len(s)
        for i in range(n):
            ch=s[i]
            if ch in "AEIOUaeiou":
                if ord(ch)>=65 and ord(ch)<=90:
                    caps+=ch
                else:
                    sms+=ch
        vowels = "".join(sorted(caps) + sorted(sms))
        v_idx = 0
        for i in range(n):
            ch=s[i]
            if ch in "AEIOUaeiou":
                res+=vowels[v_idx]
                v_idx+=1
            else:
                res+=ch   
        return res