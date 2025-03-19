class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        openers = ["{", "[", "("]
        closers = ["}", "]", ")"]
        main_str = []
        for i, ch in enumerate(s): 
            if ch in openers:
                main_str.append(ch)
            else:
                if len(main_str)>0 and openers[closers.index(ch)] == main_str[-1]:
                    main_str.pop()
                else:
                    return False
        return len(main_str) == 0

print(Solution().isValid("(){}}{"))
# print(Solution().isValid("()[]{}"))
# print(Solution().isValid("(]"))
# print(Solution().isValid("([])"))