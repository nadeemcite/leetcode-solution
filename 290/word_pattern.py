class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        patterns = [*pattern]
        final_dict = {}
        word_dict = {}
        words = s.split(' ')
        if len(patterns)!=len(words):
            return False
        for i, word in enumerate(words):
            # print(i, word, patterns[i])
            if word in word_dict:
                if word_dict[word] !=  patterns[i]:
                    return False
            else:
                if patterns[i] in final_dict:
                    return False
                final_dict[patterns[i]] = word
                word_dict[word] = patterns[i]
        return True

if __name__ == "__main__":
    ptr = Solution()
    pattern = "abba"
    s = "dog cat cat dog"
    print(ptr.wordPattern(pattern,s))