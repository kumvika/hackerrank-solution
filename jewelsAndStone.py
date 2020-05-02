class Solution(object):
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        jewel_dict = {}
        sum_stone = 0
        for jewel in S:
            if jewel in jewel_dict:
                jewel_dict[jewel] += 1
            else:
                jewel_dict[jewel] = 1
        for jewel in J:
            if jewel in jewel_dict:
                sum_stone += jewel_dict[jewel]
        return sum_stone

# J = "aA"
# S = "aAAbbbb"
#Output = 3

# J = "z"
# S = "ZZ"
#Output = 0
    
