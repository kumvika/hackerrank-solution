class Solution(object):
    def decompressRLElist(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        output_list = []
        for i in range(0, len(nums),2):
            new_arr = []
            new_arr.append(nums[i+1])
            output_list += (nums[i]*new_arr)
        return output_list