# problem url - https://neetcode.io/problems/spiral-matrix

class Solution:


    def spiralOrder(self, matrix):
        final = []
        right_border = len(matrix[0])
        left_border = 0
        top_border = 0
        bottom_border = len(matrix)
        while left_border < right_border and top_border < bottom_border:
            # go right
            for i in range(left_border, right_border):
                final.append(matrix[top_border][i])
            top_border += 1

            for i in range(top_border, bottom_border):
                final.append(matrix[i][right_border-1])
            right_border -= 1

            if not (left_border < right_border and top_border < bottom_border):
                break

            for i in range(right_border-1, left_border-1, -1):
                final.append(matrix[bottom_border-1][i])
            bottom_border -= 1

            for i in range(bottom_border-1, top_border-1, -1):
                final.append(matrix[i][left_border])
            left_border += 1

        return final


solution = Solution()
matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]

print(solution.spiralOrder(matrix))