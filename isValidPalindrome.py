def isPalindrome(s):
    """
    :type s: str
    :rtype: bool
    """
    raw_str = ""
    for char in s.lower():
        if char.isalnum():
            raw_str += char
    return (raw_str==raw_str[::-1])

print(isPalindrome("A man, a plan, a canal: Panama"))