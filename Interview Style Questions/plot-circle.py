import math

'''
In this question you are given a 2D matrix populated with zeros.
Given x and y coordinates acting as 'center of the circle' and the radius of the circle,
your goal is to draw the circumfrence of the circe around the the radius by changing the 0's in the matrix to 1's
'''

'''
Solution:
Iterate through the matrix, if the euclidean distance between the curent coordinates and the center coordinates is equal the radius, change it to 1.
'''

class Solution:

    def image_printer(self, img):
        for i in img:
            for j in i:
                if j  == 0:
                    print(" ")
                else:
                    print(".")

    def eucd_distance(self, x1, y1, x2, y2):
        return math.sqrt((x2-x1)**2 + (y2-y1)**2)


    def plotCircle(self, img, cx, cy, radius):
        for y in range(len(img)):
            for x in range(len(img[y])):
                if self.eucd_distance(x, y, cx, cy) == radius:
                    img[y][x] = 1
        



img = [[0 for _ in range(10)] for _ in range(10)]
print(img)
solution = Solution()
solution.image_printer(solution.plotCircle(img, 4, 4, 2))