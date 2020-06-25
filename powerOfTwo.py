import math

class Solution:
    def powerOfN(self, num, power=2):
        """
        Function to check if the input number
        is power of another number
        """
        if num == 0:
            return false
        # (N)^x = Num
        # x = log(Num)/ log(N)
        x = math.log10(num)/math.log10(power)
        if math.floor(x) == math.ceil(x):
            return True
        else:
            return False

s = Solution()
num = 27
print(s.powerOfN(num))