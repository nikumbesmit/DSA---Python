# Leetcode - 48. Rotate Image

class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        
        n = len(matrix)

        for i in range(n):
            for j in range(i, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        
        for i in range(n):
            matrix[i].reverse()


if __name__ == "__main__":
    n = int(input("Enter matrix dimension (n for an n x n matrix): "))
    
    matrix = []
    print(f"Enter the {n} rows (space-separated integers for each row):")
    for _ in range(n):
        row = list(map(int, input().split()))
        matrix.append(row)
        
    sol = Solution()
    sol.rotate(matrix)
    
    print("\nRotated Matrix (90 degrees clockwise):")
    for row in matrix:
        print(row)
