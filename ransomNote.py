class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        ransomDict = {}
        magazineDict = {}
        for char in ransomNote:
            if char in ransomDict:
                ransomDict[char] += 1
            else:
                ransomDict[char] = 1
                
        for char in magazine:
            if char in magazineDict:
                magazineDict[char] += 1
            else:
                magazineDict[char] = 1
        for char in ransomNote:
            if ((char in ransomNote) and (char in magazine)):
                if ransomDict[char] > magazineDict[char]:
                    return False
            else:
                    return False
        return True

#ransomNote = "bg"
#magazine = "efjbdfbdgfjhhaiigfhbaejahgfbbgbjagbddfgdiaigdadhcfcj"