# Given a positive integer num consisting only of digits 6 and 9.
# Return the maximum number you can get by changing at most one digit (6 becomes 9, and 9 becomes 6).

class Solution(object):
    def maximum69Number (self, num):
        """
        :type num: int
        :rtype: int
        """
        num_str = str(num)
        max_num = num
        for i in range(len(num_str)):
            if (i != (len(num_str)-1)):
                if (num_str[i] == '6'):
                    new_num = num_str[0:i] + "9" + num_str[i+1:]
                if (num_str[i] == '9'):
                    new_num = num_str[0:i] + "6" + num_str[i+1:]
            else:
                if (num_str[i] == '6'):
                    new_num = num_str[0:i] + "9"
                if (num_str[i] == '9'):
                    new_num = num_str[0:i] + "6"
            if int(new_num) > max_num:
                max_num = int(new_num)
        return max_num

#num = 999
num = 9996
a = Solution()
print(a.maximum69Number(num))

