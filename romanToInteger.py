class Solution:
    """
    Given an string in roman no format (s)
    your task is to convert it to integer
    """
    def romanToInt(self, roman):
        roman_nums = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        result = 0
        temp = 0
        roman_list = list(roman)
        last_idx = len(roman_list)-1
        # Iterating through each char of the Roman Number from Left to Right
        for i in range(last_idx,-1,-1):
            curr_roman_char = roman_nums[roman_list[i]]
            if curr_roman_char > temp:
                result +=  curr_roman_char
            else:
                result -= curr_roman_char
            temp = curr_roman_char
        return result

s = Solution()
nums = "IX"
print(s.romanToInt(nums))


