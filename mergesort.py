class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        n_counter = 0
        m_counter = 0
        i = 0
        while n_counter<n:
            if m_counter<m and nums1[i] >= nums2[n_counter]:
                nums1.insert(i, nums2[n_counter])
                n_counter+=1
            elif m_counter < m and nums1[i] < nums2[n_counter]:
                m_counter+=1
            elif m_counter >=m:
                nums1.insert(i, nums2[n_counter])
                n_counter+=1
            i += 1
        del nums1[m+n:]

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
    

s = Solution()
nums1=[1,0]
s.merge(nums1, 1,[2],1)
print(nums1)