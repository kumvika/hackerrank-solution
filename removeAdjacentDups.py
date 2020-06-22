class Solution:
    def removeAdjacentDupStr(self, input_str):
        result = []
        for i in range(len(input_str)):
            current_char = input_str[i]
            if (result and (result[-1] == current_char)):
                result.pop()
            else:
                result.append(input_str[i])
            print("String till now is = " + str(result))
        return result

s = Solution()
#ip = "abbbbcddde"
ip = "acaaabbbacdddd"

print(s.removeAdjacentDupStr(ip))