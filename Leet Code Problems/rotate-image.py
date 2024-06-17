# problem url - https://leetcode.com/problems/rotate-image/description/


class Solution:

    def diagonal_flip(self, matrix):
        flipped = [[False for _ in range(len(matrix))] for _ in range(len(matrix))]
        i = 0
        while i < len(matrix):
            j = 0
            while j < len(matrix[i]):
                if i != j and not flipped[i][j] and not flipped[j][i]:
                    matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
                    flipped[i][j] = True
                    flipped[j][i] = True
                j+=1
            i += 1

    def horizontal_flip(self, matrix):
        i = 0
        while i < len(matrix):
            matrix[i] = matrix[i][::-1]
            i += 1


        

    def rotate(self, matrix) -> None:
        self.diagonal_flip(matrix)
        self.horizontal_flip(matrix)



solution = Solution()

matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(matrix)
solution.diagonal_flip(matrix)
print(matrix)
solution.horizontal_flip(matrix)
print(matrix)