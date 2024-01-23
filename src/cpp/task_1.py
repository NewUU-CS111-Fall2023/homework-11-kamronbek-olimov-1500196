def findWays(nums, target):
    memo = {}
    def dfs(index, current_sum):
        if index == len(nums):
            if current_sum == target:
                return 1
            return 0
        if (index, current_sum) in memo:
            return memo[(index, current_sum)]
        ways = dfs(index + 1, current_sum + nums[index]) + dfs(index + 1, current_sum - nums[index])
        memo[(index, current_sum)] = ways
        return ways
    return dfs(0, 0)
nums = list(map(int, input("nums = ").split()))
target = int(input("target = "))
result = findWays(nums, target)
print(result)
