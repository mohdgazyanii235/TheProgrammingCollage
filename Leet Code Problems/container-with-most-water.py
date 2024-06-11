# problem url - https://leetcode.com/problems/container-with-most-water/description/

class Solution:
    # two pointer solution:

    def maxArea(self, height) -> int:
        max_area = 0
        max_tuple = ()
        i = 0
        j = len(height) - 1

        while i < j:
            temp_area = min(height[i], height[j]) * (j-i)
            if temp_area > max_area:
                max_area = temp_area
                max_tuple = (height[i], height[j])

            if height[i] < height[j]:
                i += 1
            else:
                j -=1 
        
        print(max_tuple)
        return max_area
    

solution = Solution()
print(solution.maxArea([1,8,6,2,5,4,8,3,7]))