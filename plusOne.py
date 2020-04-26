class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        input_digit = "".join (str(digit) for digit in digits)
        output_digit = int(input_digit) + 1
        op_arr =  [ int(digit) for digit in str(output_digit) ]
        return op_arr