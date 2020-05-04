class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        binary_num = []
        
        while(num>0):
            rem = num % 2
            num = num //2
            binary_num.append(rem)
        complement_num = 0
        for i in range(len(binary_num)):
            if binary_num[i] == 1:
                complement_num += (0 * (2**i))
            else:
                complement_num += (1 * (2**i))
        return complement_num


print(findComplement(2))

