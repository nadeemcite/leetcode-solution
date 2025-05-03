import bisect

class Solution:
    def maxTaskAssign(self, tasks, workers, pills, strength):
        # Sort both lists so we can match weakest tasks with strongest workers
        tasks.sort()
        workers.sort()
        
        low, high = 0, min(len(tasks), len(workers))
        
        # Binary search for the largest k tasks we can assign
        while low < high:
            candidate = (low + high + 1) // 2
            pills_used = 0
            # Take the top `candidate` strongest workers
            pool = workers[-candidate:]
            possible = True
            
            # Try to assign the hardest `candidate` tasks
            for req in reversed(tasks[:candidate]):
                if pool and pool[-1] >= req:
                    # Strongest available worker can handle without a pill
                    pool.pop()
                else:
                    # Need to use a pill: find the first worker who, with pill, can handle it
                    idx = bisect.bisect_left(pool, req - strength)
                    if pills_used == pills or idx == len(pool):
                        possible = False
                        break
                    pills_used += 1
                    pool.pop(idx)
            
            if possible:
                low = candidate
            else:
                high = candidate - 1
        
        return low
