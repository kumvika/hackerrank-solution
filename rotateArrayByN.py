class Solution:
    def rotateArray(self, nums, direction="left", n=1):
        while(n>0):
            if direction == "left":
                first_idx = nums[0]
                for i in range(1,len(nums)):
                    nums[i-1] = nums[i]
                nums[len(nums)-1] = first_idx
            else:
                last_idx = nums[len(nums)-1]
                for i in range(len(nums)-1, 0,-1):
                    nums[i] = nums[i-1]
                nums[0] = last_idx
            n -= 1
        return "".join(nums)

"""
Given two strings a and b.
The task is to find if a string 'a' can be obtained
by rotating another string 'b' by 2 places.
"""

s = Solution()
ip = "amazon"
op = "azonam"
nums = list(ip)
print(s.rotateArray(nums,n=2))
if op == s.rotateArray(nums,n=2):
    print(1)
else:
    print(0)
        
