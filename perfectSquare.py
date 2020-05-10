class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num < 2:
            return True
        left = 0
        right = num
        while(right > left):
            mid = left + (right - left)/2
            if mid*mid == num:
                return mid
            elif mid*mid > num:
                right = mid
            else:
                left = mid + 1
        return False

#num = 4410000
#num = -4
num = 1
#num = 2147395600
#num = 14
#print(isPerfectSquare(num))
    