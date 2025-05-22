import heapq

class Solution(object):
    def maxRemoval(self, nums, queries):
        n, m = len(nums), len(queries)
        starts = [[] for _ in range(n)]
        for l, r in queries:
            starts[l].append(r)

        heap = []            # max-heap (store -r) of active queries
        diff = [0] * (n + 1) # difference array
        cur_dec = 0          # prefix sum of diff
        used = 0             # how many queries we actually pick

        for i in range(n):
            # 1) Add new intervals that start at i
            for r in starts[i]:
                heapq.heappush(heap, -r)

            # 2) Purge any that no longer cover i
            while heap and -heap[0] < i:
                heapq.heappop(heap)

            # 3) Account for decrements so far
            cur_dec += diff[i]
            need = nums[i] + cur_dec

            # 4) While we still need more at i, keep picking the farthest-reaching valid interval
            while need > 0:
                # re-purge before each pop
                while heap and -heap[0] < i:
                    heapq.heappop(heap)
                if not heap:
                    return -1

                r = -heapq.heappop(heap)
                used += 1

                # apply its “-1” to [i..r] via diff array
                diff[i]    -= 1
                diff[r+1]  += 1
                cur_dec    -= 1
                need       -= 1

        # we used `used` queries; the rest can be removed
        return m - used
    

print(Solution().maxRemoval([2,0,2], [[0,2],[0,2],[1,1]]))
print(Solution().maxRemoval([1,1,1,1], [[1,3],[0,2],[1,3],[1,2]]))
print(Solution().maxRemoval([1,2,3,4], [[0,3]]))
print(Solution().maxRemoval([0,3], [[0,1],[0,0],[0,1],[0,1],[0,0]]))

print(Solution().maxRemoval([0,0,3], [[0,2],[1,1],[0,0],[0,0]]))

