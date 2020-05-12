def singleNonDuplicate(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    nums_dict = {}
    for num in nums:
        if num in nums_dict:
            nums_dict[num] += 1
        else:
            nums_dict[num] = 1
    
    for key, val in nums_dict.items():
        if val == 1:
            return key

#nums = [3,3,7,7,10,11,11]
#nums = []
nums = [1,1,2,3,3,4,4,8,8]
print(singleNonDuplicate(nums))
