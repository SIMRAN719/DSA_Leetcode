class Solution(object):
    def spiralOrder(self, matrix):
        col=len(matrix[0])
        row=len(matrix)
        rc,cc=0,0
        a=[]
        temp='R'
        if (row==1):
            x=1
        elif (row<=col):
            x=2*row-1
        elif(row>col):
            x=col*2
        for i in range(x):
            if temp=='R':
                for q in range(rc,col):
                    a.append(matrix[rc][q])
                temp='D'
                rc+=1
            elif temp=='D':
                for j in range(rc,row):
                    a.append(matrix[j][col-1])
                temp='L'
                col-=1
            elif temp=='L':
                for w in range(col-1,cc-1,-1):
                    a.append(matrix[row-1][w])
                temp='U'
                row-=1
            elif temp=='U':
                for k in range(row-1,rc-1,-1):
                    a.append(matrix[k][cc])
                temp='R'
                cc+=1
        return a