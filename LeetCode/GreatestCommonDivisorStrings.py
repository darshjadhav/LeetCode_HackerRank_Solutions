class Solution:
    def gcdfunc(self, shortstr, longstr):
        shortlen, longlen = len(shortstr), len(longstr)
        gcdstr = ""
        for i in range(1, shortlen+1):
            if longlen % i == 0 and shortlen % i == 0:
                if (shortstr[:i] * int((shortlen/len(shortstr[:i]))) == shortstr) and (shortstr[:i] * int((longlen/len(shortstr[:i]))) == longstr):
                    gcdstr = shortstr[:i]
        return gcdstr





    def gcdOfStrings(self, str1: str, str2: str) -> str:


        len1, len2 = len(str1), len(str2)

        if len1 < len2:
            gcdstr = self.gcdfunc(str1, str2)
        elif len2 <= len1:
            gcdstr = self.gcdfunc(str2, str1)


        return gcdstr
