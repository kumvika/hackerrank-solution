class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        import functools
        output = []
        for i in range(len(nums)):
            output.append(functools.reduce(lambda x,y:x+y,nums[0:i+1]))
        return output
