def getLeaders(nums):
    leaders = []
    if not nums:
        return False
    for i in range(len(nums)):
        flag = True
        for j in range(i+1, len(nums)):
            if nums[i] < nums[j]:
                flag = False
                break
        if flag == True:
            leaders.append(nums[i])
    return leaders

#nums = [16,17,4,3,5,2]
#nums = [1, 2, 3, 4, 0]
nums = [7, 4, 5, 7, 3]
print(getLeaders(nums))
