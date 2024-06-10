class Solution(object):
    def reverseWords(self, s):
        l=s.split()
        #l=l[::-1]
        l.reverse()
        s=" ".join(l)
        return s