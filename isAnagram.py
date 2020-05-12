def isAnagram(s1, s2):
    if len(s1) != len(s2):
        return False
    else:
        if sorted(s1) == sorted(s2):
            return True
        else:
            return False

print(isAnagram("vikash", "chivas"))
