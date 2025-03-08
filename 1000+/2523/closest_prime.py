class Solution(object):
    def closestPrimes(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        all_primes = [True] * (1+right)
        
        for i in range(2, int(right**0.5)+1):
            j = 2*i
            while j <= right:
                all_primes[j] = False
                j+=i
        primes = []
        for i in range(left, right+1):
            if all_primes[i]:
                print(i)
                primes.append(i)
        if len(primes) >= 2:
            gaps = {}
            for i, prime in enumerate(primes[:-1]):
                gap = primes[i+1]  - prime
                if gap not in gaps:
                    gaps[gap] = [prime, primes[i+1]]
            return gaps[min(gaps.keys())]
        return [-1, -1]
        

print(Solution().closestPrimes(19,31))