class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        l_index = len(digits) - 1
        add_sum = 1
        index_val = 0
        while l_index>-1:
            index_val = digits[l_index] + add_sum
            if digits[l_index]<0:
                break
            add_sum = index_val // 10
            digits[l_index] = index_val % 10
            l_index -= 1
        if l_index == -1 and index_val > 9:
            digits.insert(0, add_sum)
        return digits
    
if __name__ == "__main__":
    ptr = Solution()
    print(ptr.plusOne([9,9]))