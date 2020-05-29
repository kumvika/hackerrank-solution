def compressStr(s):
    count = 0
    current_char = s[0]
    s += ' '
    compressed_str = ""
    for char in s:
        if char == current_char:
            count += 1
        else:
            compressed_str += (str(count) + current_char)
            current_char = char
            count = 1
    return compressed_str

s = "AAAAAABCCDEEEE"
print(compressStr(s))
