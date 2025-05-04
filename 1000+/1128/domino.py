class Solution(object):
    def numEquivDominoPairs(self, dominoes):
        from collections import defaultdict

        count = defaultdict(int)
        pairs = 0

        for a, b in dominoes:
            key = tuple(sorted((a, b)))
            pairs += count[key]
            count[key] += 1
        return pairs