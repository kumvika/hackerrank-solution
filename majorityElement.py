class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        threshold = len(nums)//2
        num_frequency = {}
        for num in nums:
            if num in num_frequency:
                num_frequency[num] += 1
            else:
                num_frequency[num] = 1
        for key, value in num_frequency.items():
            if value > threshold:
                return key