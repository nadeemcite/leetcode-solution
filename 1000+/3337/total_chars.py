class Solution(object):
    def lengthAfterTransformations(self, s, t, nums):
        """
        :type s: str
        :type t: int
        :type nums: List[int]
        :rtype: int
        """
        mod = 10**9 + 7

        # Build the 26×26 transformation matrix M where
        # M[c][d] = 1 if character c transforms into character d in one step.
        M = [[0]*26 for _ in range(26)]
        for c in range(26):
            k = nums[c]
            for i in range(1, k+1):
                M[c][(c + i) % 26] = 1

        # Multiply two 26×26 matrices
        def mat_mult(A, B):
            C = [[0]*26 for _ in range(26)]
            for i in range(26):
                Ai = A[i]
                Ci = C[i]
                for k in range(26):
                    a = Ai[k]
                    if a:
                        Bk = B[k]
                        # unroll inner sum
                        for j in range(26):
                            Ci[j] = (Ci[j] + a * Bk[j]) % mod
            return C

        # Fast exponentiation of M to the power p
        def mat_pow(mat, p):
            # start with identity
            result = [[1 if i==j else 0 for j in range(26)] for i in range(26)]
            base = mat
            while p:
                if p & 1:
                    result = mat_mult(result, base)
                base = mat_mult(base, base)
                p >>= 1
            return result

        # Compute M^t
        M_t = mat_pow(M, t)

        # f_t[c] = total length contributed by a single 'a'+c after t transforms
        # = sum of row c in M_t times f_0 (which is all 1’s)
        f_t = [sum(row) % mod for row in M_t]

        # Sum up contributions for each character in the original string
        ans = 0
        for ch in s:
            ans = (ans + f_t[ord(ch) - ord('a')]) % mod

        return ans
    

print(Solution().lengthAfterTransformations("abcyy", 2, [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2]))
print(Solution().lengthAfterTransformations("azbk", 1, [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2]))