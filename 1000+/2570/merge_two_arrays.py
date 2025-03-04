class Solution(object):
    def mergeArrays(self, nums1, nums2):
        """
        :type nums1: List[List[int]]
        :type nums2: List[List[int]]
        :rtype: List[List[int]]
        """
        p1 = 0
        p2 = 0
        n1 = len(nums1)
        n2 = len(nums2)
        final_list = []
        for i in range(n1+n2):
            if p1 < n1 and p2 < n2:
                min_id = min(nums1[p1][0], nums2[p2][0])
            elif p1 < n1:
                min_id = nums1[p1][0]
            else:
                min_id = nums2[p2][0]
            final_list.append([min_id, 0])
            if p1 < n1 and nums1[p1][0] == min_id:
                final_list[i][1] += nums1[p1][1]
                p1 += 1
            if p2 < n2 and nums2[p2][0] == min_id:
                final_list[i][1] += nums2[p2][1]
                p2 += 1
            if p1 + p2 == n1 + n2:
                break
        return final_list
    
print(Solution().mergeArrays(
    [[2,4],[3,6],[5,5]],
    [[1,3],[4,3]],
))
