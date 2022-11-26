class Solution:
    def generate(self, n: int) -> List[List[int]]:
        sol = [[1]*i for i in range(1, n+1)] 
        for i in range(1,n):
            for j in range(1,i):
                sol[i][j]=sol[i-1][j] + sol[i-1][j-1]
        return sol