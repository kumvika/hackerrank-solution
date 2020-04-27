class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        hash_map = {}
        for i in range(len(numbers)):
            complement = target - numbers[i]
            if complement not in hash_map:
                hash_map[numbers[i]] = i
            else:
                return hash_map[complement]+1,i+1