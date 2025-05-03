class Solution(object):
    def minDominoRotations(self, tops, bottoms):
        """
        :type tops: List[int]
        :type bottoms: List[int]
        :rtype: int
        """
        import sys
        def rotations(x):
            rot_a = rot_b = 0
            for t, b in zip(tops, bottoms):
                if t != x and b != x:
                    return sys.maxsize
                elif t != x:
                    rot_a += 1
                elif b != x:
                    rot_b += 1
            return min(rot_a, rot_b)

        candidates = {tops[0], bottoms[0]}
        ans = min(rotations(x) for x in candidates)
        return ans if ans != sys.maxsize else -1
    
print(Solution().minDominoRotations([2,1,2,4,2,2], [5,2,6,2,3,2]))
print(Solution().minDominoRotations([3,5,1,2,3], [3,6,3,3,4]))