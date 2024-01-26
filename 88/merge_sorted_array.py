class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        i = m - 1
        j = n - 1
        k = m + n - 1
        while j >= 0:
            if i >= 0 and nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1

    def my_merge(self, l, r):
        result = []
        while len(l) and len(r):
            if l[0] <= r[0]:
                extracted = l.pop(0)
            else:
                extracted = r.pop(0)
            result.append(extracted)
        result.extend(l)
        result.extend(r)
        return result

        
    def merge_sort(self, arr):
        if len(arr)<2:
            return arr
        mid = len(arr)//2
        left_merge = self.merge_sort(arr[:mid])
        right_merge = self.merge_sort(arr[mid:])
        return self.my_merge(left_merge, right_merge)
    

if __name__ == "__main__":
    s = Solution()
    nums1=[1,0]
    s.merge(nums1, 1,[2],1)
    print(nums1)