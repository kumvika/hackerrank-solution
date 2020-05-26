# Method 1: with T.C - o(N) and S.C O(N)
def rearrangeMaxMin(nums):
    # Time Complexity O(N)
    # Space Complexity O(N)
    count = 0
    i = 0
    j = len(nums) - 1
    output_nums = []
    while(i<=j):
        if count % 2 == 0:
            output_nums.append(nums[j])
            j -= 1
        else:
            output_nums.append(nums[i])
            i += 1
        count += 1
    return output_nums

# Method 2: with T.C - o(N2) and S.C O(1)
def rearrangeMaxMin2(nums):
    # Time Complexity O(N2)
    # Space Complexity O(1)
    for i in range(len(nums)-1):
        if i % 2 == 0:
            max_num = nums[len(nums)-1]
            temp = nums[i]
            for j in range(len(nums)-2, i, -1):
                nums[j+1] = nums[j]
            nums[i] = max_num
            nums[i+1] = temp
    return nums
            

nums = [1,2,4,5,9]
#nums = [1,2,3,4]
print(rearrangeMaxMin2(nums))


