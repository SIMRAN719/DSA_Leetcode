class Solution(object):
    def rotate(self, matrix):
        row=len(matrix)
        col=len(matrix[0])
        for i in range(col):
            roll=col-1
            for j in range(row):
                temp=matrix[roll][0]
                matrix[i].append(temp)
                matrix[roll].pop(0)
                roll-=1