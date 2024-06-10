class Solution(object):
    def setZeroes(self, matrix):
        row=len(matrix)
        col=len(matrix[0])
        ind=col-1
        a=[]
        for i in range(row):
            for j in range(col):
                if matrix[i][j]==0:
                    a.append([i,j])
        for i in range(len(a)):
            for j in range(2):
                temp1=a[i][0]
                for m in range(col):
                    matrix[temp1][m]=0
                temp2=a[i][1]
                for p in range(row):
                    matrix[p][temp2]=0 