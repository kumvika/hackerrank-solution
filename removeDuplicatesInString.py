# Input:
# First line of the input is the number of test cases T. And first line of test case contains a string.

# Output: 
# Modified string without duplicates and same order of characters.

def removeDuplicateChar(s):
    output_str = ''
    for char in s:
        if char not in output_str:
            output_str += char
    return output_str.strip()

test_cases = int(input())
for test_case in range(test_cases):
    input_str = raw_input()
    print(removeDuplicateChar(input_str))

#s = "geeksforgeeks"
#s = "geeks for geeks"