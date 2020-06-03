class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        capacity = 0
        for i in range(1, len(height)-1):
            left_max = max(height[0:(i+1)])
            right_max = max(height[i:])
            capacity += (min(left_max, right_max) - height[i])
        return capacity

height = [0,1,0,2,1,0,1,3,2,1,2,1]
#height = [2,0,2]
s = Solution()
print(s.trap(height))