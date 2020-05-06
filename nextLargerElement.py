def nextLargerElement(nums):
    if len(nums) > 1:
        output_arr = []
        for i in range(len(nums)-1):
            found = 0
            for j in range(i+1, len(nums)):
                if nums[j] > nums[i]:
                    found = 1
                    output_arr.append(nums[j])
                    break
            if found == 0:
                output_arr.append(-1)
        output_arr.append(-1)
        return output_arr
    else:
        return [-1]

#nums = [4,3,2,1]
#nums = [1,3,2,4]
#nums = [1,4]
#nums = [1,1]

test_cases = int(raw_input())
for test_case in range(test_cases):
    no_of_element = int(raw_input())
    input_arr = list(map(int, raw_input().split()))
    print(nextLargerElement(input_arr))