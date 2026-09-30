# Leetcode - 73. Set Matrix Zeroes

class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        
        if not matrix:
            return None
            
        m, n = len(matrix), len(matrix[0])
        zero_rows = set()
        zero_col = set()
        
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    zero_rows.add(i)
                    zero_col.add(j)
                    
        for i in range(m):
            for j in range(n):
                if i in zero_rows or j in zero_col:
                    matrix[i][j] = 0
                    

if __name__ == "__main__":

    m = int(input("Enter number of rows: "))
    
    matrix = []
    print(f"Enter the {m} rows (space-separated integers for each row):")
    for _ in range(m):
        row = list(map(int, input().split()))
        matrix.append(row)
        
    sol = Solution()
    sol.setZeroes(matrix)
    
    print("\nMatrix after setting zeroes:")
    for row in matrix:
        print(row)
