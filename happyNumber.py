class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        while (n > 0):
            num_str = str(n)
            sum_of_square = 0
            for num in num_str:
                sum_of_square += (int(num) ** 2)
            if sum_of_square == 1:
                return True
            elif sum_of_square == 4:
                return False
            else:
                n = sum_of_square

#print(isHappy(19))
#print(isHappy(20))
#print(isHappy(1))