class Solution:
    def isRectangleOverlap(self, rec1, rec2) -> bool:
        reca_x1, reca_y1, reca_x2, reca_y2 = rec1
        recb_x1, recb_y1, recb_x2, recb_y2 = rec2

        # Check if one rectangle is to the left of the other
        if reca_x2 <= recb_x1 or recb_x2 <= reca_x1:
            return False

        # Check if one rectangle is above the other
        if reca_y2 <= recb_y1 or recb_y2 <= reca_y1:
            return False

        return True
        




solution = Solution()
print(solution.isRectangleOverlap([7,8,13,15], [10,8,12,20]))