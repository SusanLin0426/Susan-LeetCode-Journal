def unique_paths(m: int, n: int) -> int:
    """
    62. Unique Paths
    DP (1D rolling): dp[j] = number of ways to reach current cell in this row.
    Transition: dp[j] += dp[j-1]  (from top + from left)
    Time: O(m*n), Space: O(n)
    """
    # edge cases
    if m <= 0 or n <= 0:
        return 0

    dp = [1] * n            # first row: only from left
    for _ in range(1, m):   # row 1..m-1
        for j in range(1, n):
            dp[j] += dp[j - 1]
    return dp[-1]
