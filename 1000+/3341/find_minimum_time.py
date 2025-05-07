import heapq

class Solution:
    def minTimeToReach(self, moveTime):
        n, m = len(moveTime), len(moveTime[0])
        dist = [[float('inf')] * m for _ in range(n)]
        dist[0][0] = 0
        
        pq = [(0, 0, 0)]
        dirs = [(1,0),(-1,0),(0,1),(0,-1)]
        
        while pq:
            t, i, j = heapq.heappop(pq)
            if t > dist[i][j]:
                continue
            if i == n-1 and j == m-1:
                return t
            
            for di, dj in dirs:
                ni, nj = i + di, j + dj
                if 0 <= ni < n and 0 <= nj < m:
                    depart = max(t, moveTime[ni][nj])
                    arrive = depart + 1
                    if arrive < dist[ni][nj]:
                        dist[ni][nj] = arrive
                        heapq.heappush(pq, (arrive, ni, nj))
        return -1
    
print(Solution().minTimeToReach([[0,4],[4,4]]))
print(Solution().minTimeToReach([[0,0,0],[0,0,0]]))
print(Solution().minTimeToReach([[0,1],[1,2]]))