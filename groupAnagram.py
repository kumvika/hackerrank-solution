class Solution(object):
    def sortChar(self, s):
        sorted_char = sorted(s)
        sorted_str = "".join(sorted_char)
        return sorted_str

    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        local_list = {}
        for word in strs:
            word_list = []
            sorted_word = self.sortChar(word)
            if sorted_word not in local_list:
                word_list.append(word)
                local_list[sorted_word] = word_list
            else:
                local_list[sorted_word].append(word)
        return(local_list.values())
    
#strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
