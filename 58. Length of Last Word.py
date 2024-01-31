class Solution(object):
    def lengthOfLastWord(self, s):
        l=s.split()
        a=len(l)
        return len(l[a-1])  