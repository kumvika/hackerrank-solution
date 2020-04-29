class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        longest_prefix = ""
        if len(strs) > 0:
            longest_word = min(strs, key=len)
            for i in range(len(longest_word)):
                j = 0
                for k in range(len(strs)):
                    if strs[k][i] == longest_word[i]:
                        j += 1
                if j == len(strs):
                    longest_prefix += longest_word[i]
                else:
                    return longest_prefix
            return longest_prefix
        else:
            return longest_prefix

# Input cases
#strs= ["flower","flow","flight"] Output = "fl"
#strs= ["aca","cba"] Output = ""