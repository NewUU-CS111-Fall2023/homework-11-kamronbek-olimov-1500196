def canPartition(nums):
    total_sum = sum(nums)

    if total_sum % 2 != 0:
        return False

    target_sum = total_sum // 2
    n = len(nums)

    dp = [[False] * (target_sum + 1) for _ in range(n + 1)]

    for i in range(n + 1):
        dp[i][0] = True

    for i in range(1, n + 1):
        for j in range(1, target_sum + 1):
            if nums[i - 1] > j:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = dp[i - 1][j] or dp[i - 1][j - nums[i - 1]]

    return dp[n][target_sum]

nums = list(map(int, input("nums: ").split()))

result = canPartition(nums)
print(result)
