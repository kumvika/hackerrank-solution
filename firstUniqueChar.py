class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        str_dict = {}
        if len(s)>=1:
            for i in range(len(s)):
                tmp = []
                if s[i] in str_dict:
                    str_dict[s[i]].append(i)
                else:
                    tmp = [i]
                    str_dict[s[i]] = tmp
            for i in range(len(s)):
                if ((s[i] in str_dict) and (len(str_dict[s[i]]) == 1)):
                    return i
            return -1
        else:
            return -1
s = ""
print(firstUniqChar(s))

