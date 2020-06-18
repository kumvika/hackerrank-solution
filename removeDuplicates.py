class Solution:

    def removeDups(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        Solution with extra space
        """
        output = []
        for i in range(0, len(nums)-1):
            if nums[i] != nums[i+1]:
                output.append(nums[i])
        output.append(nums[len(nums)-1])
        return len(output)

    def removeDupsConstSpace(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        Solution without extra space/ Constant Space
        """
        if not nums:
            return 0
        if len(nums) == 1:
            return 1
        j = 0
        for i in range(0, len(nums)-1):
            if nums[i] != nums[i+1]:
                nums[j] = nums[i]
                j += 1
        nums[j] = nums[len(nums)-1]
        return len(nums[:j+1])

if __name__== "__main__":
    #nums = [1,2,2,2,2,3,3,6,7,7,9]
    #nums = [1,1,2,3,3,7]
    nums = [1,1,2]
    s = Solution()
    print(s.removeDups(nums))
    print(s.removeDupsConstSpace(nums))
