class Solution(object):
    def countBits(self, n):
        binlist=[]
        for i in range(n+1):
            z=str(bin(i))
            x=z.count('1')
            binlist.append(x)
        return binlist     