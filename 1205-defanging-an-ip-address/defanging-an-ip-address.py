class Solution(object):
    def defangIPaddr(self, address):
        """
        :type address: str
        :rtype: str
        """
        x=address.split(".")
        ans="[.]".join(x)
        return ans