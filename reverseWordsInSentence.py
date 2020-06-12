#code
def reverseWords(input_str):
    result = ""
    word_list = input_str.split('.')
    for i in range(len(word_list)):
        result = (word_list[i] + ".") + result
    return result[:-1]
test_cases = int(input())
for test_case in range(test_cases):
    input_str = input()
    print(reverseWords(input_str))