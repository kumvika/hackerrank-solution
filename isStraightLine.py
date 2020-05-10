class Solution(object):
    def checkStraightLine(self, coordinates):
        """
        :type coordinates: List[List[int]]
        :rtype: bool
        """
        slope = self.getSlope(coordinates[0], coordinates[1])
        for i in range(2, len(coordinates)):
            curr_slope = self.getSlope(coordinates[0], coordinates[i])
            if slope != curr_slope:
                return False
        return True

    def getSlope(self, p1, p2):
        y_diff = p2[1] - p1[1]
        x_diff = p2[0] - p1[0]
        if (x_diff == 0):
            return 0;
        m = float(y_diff) / x_diff
        return m
        

# coordinates = [[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]] #False
# coordinates = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]] # True
# coordinates = [[-7,-3],[-7,-1],[-2,-2],[0,-8],[2,-2],[5,-6],[5,-5],[1,7]] #False