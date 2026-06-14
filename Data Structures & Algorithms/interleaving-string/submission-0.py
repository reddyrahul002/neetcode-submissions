class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        m, n = len(s1), len(s2)
        if m + n != len(s3):
            return False

        memo = {}
        def check(i, j):
            if i == m and j == n:
                return True
            if (i, j) in memo:
                return memo[(i, j)]
            k = i + j
            result = False
            if i < m and s1[i] == s3[k]:
                result = result or check(i+1, j)
            if j < n and s2[j] == s3[k]:
                result = result or check(i, j+1)
            memo[(i, j)] = result
            return result

        return check(0, 0)