def isValidPhoneNumber(num):
    import re
    pattern = re.compile("^[7-9][0-9]{9}$")
    if len(num) < 10:
        return("NO")
    if (pattern.match(num)):
        return("YES")
    else:
        return("NO")

test_cases = int(raw_input())

for test_case in range(test_cases):
    input_num = raw_input()
    print(isValidPhoneNumber(input_num))