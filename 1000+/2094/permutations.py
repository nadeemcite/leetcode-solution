from itertools import permutations

class Solution(object):
    def findEvenNumbers(self, digits):
        res = set()
        for a, b, c in permutations(digits, 3):
            if a != 0 and c % 2 == 0:
                num = 100 * a + 10 * b + c
                res.add(num)
        return sorted(res)

solution = Solution()
print(solution.findEvenNumbers([2, 1, 3, 0]))
print(solution.findEvenNumbers([2, 2, 8, 8, 2]))
print(solution.findEvenNumbers([3, 7, 5]))