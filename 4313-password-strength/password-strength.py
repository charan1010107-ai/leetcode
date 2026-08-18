class Solution(object):
    def passwordStrength(self, password):
        
        velqurimex = password
        
        lower = set()
        upper = set()
        digit = set()
        special = set()

        for ch in velqurimex:
            
            if ch.islower():
                lower.add(ch)

            elif ch.isupper():
                upper.add(ch)

            elif ch.isdigit():
                digit.add(ch)

            elif ch in "!@#$":
                special.add(ch)

        return (len(lower) * 1 +
                len(upper) * 2 +
                len(digit) * 3 +
                len(special) * 5)