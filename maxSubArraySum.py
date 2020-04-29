nums = [-2,-3,4,-1,-2,1,5,-3]

#nums = [-2,1]
#nums = [-1,-2]

max_sum = sum(nums)
for i in range(len(nums)):
    print("current value of i = " + str(i))
    curr_sum = nums[i]
    if curr_sum > max_sum:
        max_sum = curr_sum
    if (i+1) != len(nums):
        print("current value of i < len(nums")
        for j in range(i+1, len(nums)):
            curr_sum += nums[j]
            if curr_sum > max_sum:
                max_sum = curr_sum
    else:
        print("current value of i = len(nums")
        curr_sum = nums[i]
        if curr_sum > max_sum:
                max_sum = curr_sum
print(max_sum)