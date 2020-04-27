class Solution(object):
    def singleNumberMethod1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        num_freq = {}
        for num in nums:
            if num in num_freq:
                num_freq[num] += 1
            else:
                num_freq[num] = 1

        for key, val in num_freq.items():
            if num_freq[key] == 1:
                return key
    def singleNumberMethod2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sum_nums = sum(nums)
        sum_set_of_nums = 2 * sum(set(nums))
        return sum_set_of_nums-sum_nums
