import heapq

class Solution(object):
    def minTimeToReach(self, moveTime):
        """
        :type moveTime: List[List[int]]
        :rtype: int
        """
        n, m = len(moveTime), len(moveTime[0])
        INF = 10**30
        dist = [[[INF, INF] for _ in range(m)] for __ in range(n)]
        dist[0][0][0] = 0
        heap = [(0, 0, 0, 0)]
        
        dirs = [(1,0),(-1,0),(0,1),(0,-1)]
        
        while heap:
            t, i, j, p = heapq.heappop(heap)
            if t > dist[i][j][p]:
                continue
            if i == n-1 and j == m-1:
                return t
            
            for di, dj in dirs:
                ni, nj = i + di, j + dj
                if 0 <= ni < n and 0 <= nj < m:
                    dt = 1 if p == 0 else 2
                    depart = max(t, moveTime[ni][nj])
                    arrive = depart + dt
                    np = 1 - p  # flip parity
                    if arrive < dist[ni][nj][np]:
                        dist[ni][nj][np] = arrive
                        heapq.heappush(heap, (arrive, ni, nj, np))
        return -1
    
print(Solution().minTimeToReach([[0,4],[4,4]]))
print(Solution().minTimeToReach([[0,0,0,0],[0,0,0,0]]))
print(Solution().minTimeToReach([[0,1],[1,2]]))