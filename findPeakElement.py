def findPeakElement(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    for i in range(1,len(nums)):
        print("current i = " + str(i))
        if (i != (len(nums)-1)):
            if ((nums[i] > nums[i-1]) and (nums[i] > nums[i+1])):
                return i
        else:
            if (nums[i] > nums[i-1]):
                return i
    return 0

#nums = [1,2]
nums = [1,2,3,1]
#nums = [1,2,1,3,5,6,4]

print(findPeakElement(nums))