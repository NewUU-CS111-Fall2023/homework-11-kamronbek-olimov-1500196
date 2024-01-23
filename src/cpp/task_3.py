def wordBreak(s, wordDict):
    n = len(s)

    wordSet = set(wordDict)

    dp = [False] * (n + 1)

    dp[0] = True

    for i in range(1, n + 1):
        for j in range(i):
            if dp[j] and s[j:i] in wordSet:
                dp[i] = True
                break

    return dp[n]

s = input("s = ")

wordDict = input("wordDict = ").split()

result = wordBreak(s, wordDict)
print(result)
