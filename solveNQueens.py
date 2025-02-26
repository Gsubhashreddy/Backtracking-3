#T(N)= O(N!) or O(N^N)
#S(N)= O(N^2)

class Solution:
    res=[]
    def solveNQueens(self, n: int) -> List[List[str]]:
        self.res=[]
        bo=[[False for i in range(n)] for j in range(n)]
        self.helper(bo,0,n)
        return self.res
        #Go through Columns
        
    def issafe(self,ar,r,c,n):
        # check up
        for i in range(0,r):
            if ar[i][c]:
                return False
        
        i=r
        j=c
        while i>=0 and j>=0:
            if ar[i][j]:
                return False
            i-=1
            j-=1
        i=r
        j=c
        while i>=0 and j<n:
            if ar[i][j]:
                return False
            i-=1
            j+=1
        return True
                
            
    def helper(self,ar,r,n):
        
        if r==n:
            t=[]
            for i in range(n):
                temp=[]
                for j in range(n):
                    if ar[i][j]==True:
                        temp.append("Q")
                    else:
                        temp.append(".")
                st="".join(temp)
                t.append(st)
            self.res.append(t)
            
        #Logic
        for j in range(n):
            if self.issafe(ar,r,j,n):
                
                ar[r][j]=True
                self.helper(ar,r+1,n)
                ar[r][j]=False
                    