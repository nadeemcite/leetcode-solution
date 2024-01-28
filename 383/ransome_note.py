class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        letters = set(ransomNote)
        for m_letter in letters:
            if magazine.count(m_letter) < ransomNote.count(m_letter):
                return False
        return True


        
if __name__ == "__main__":
    ptr = Solution()
    ransomNote = "fihjjjjei"
    magazine = "hjibagacbhadfaefdjaeaebgi"
    print(ptr.canConstruct(ransomNote,magazine))