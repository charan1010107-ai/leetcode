class Solution(object):
    def squareIsWhite(self, coordinates):
        """
        :type coordinates: str
        :rtype: bool
        """
        x=ord(coordinates[0])
        if x%2!=0 and int(coordinates[1])%2!=0:
            return False
        elif x%2==0 and int(coordinates[1])%2==0:
            return False
        else:
            return True