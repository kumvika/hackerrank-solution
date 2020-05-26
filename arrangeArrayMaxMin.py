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

nums = [1,2,4,5,9]
print(rearrangeMaxMin(nums))


