931. Minimum Falling Path Sum
Given an n x n array of integers matrix, return the minimum sum of any falling path through matrix.

A falling path starts at any element in the first row and chooses the element in the next row that is either directly below or diagonally left/right.
Specifically, the next element from position (row, col) will be (row + 1, col - 1), (row + 1, col), or (row + 1, col + 1).

Approach - 
This is simple Dynamic Programming problem where we need to maintain result of latest row and
add the result of current element and prev calculated row minimum (diagonal, below).

class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        
        rows = len(matrix)

        for i in range(rows-2, -1, -1):
            for j in range(rows):
                # for first column only one diagonal, there will no left diagonal
                if j == 0:
                    matrix[i][j] += min(matrix[i+1][j], matrix[i+1][j+1])
                # for last column only one diagonal, there will no right diagonal
                elif j == rows-1:
                    matrix[i][j] += min(matrix[i+1][j], matrix[i+1][j-1])
                else:
                    matrix[i][j] += min(matrix[i+1][j], matrix[i+1][j+1], matrix[i+1][j-1])
        At the end return min(matrix[0]) as it contain all possible paths sum and we have to return minimum sum path.
        return min(matrix[0])