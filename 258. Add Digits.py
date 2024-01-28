class Solution(object):
    def addDigits(self, num):
        sum,a=0,0
        while num>0:
            a=num%10
            num=num//10
            sum+=a
            if num==0 and sum>9:
                num=sum
                sum=0
        return sum