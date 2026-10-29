def minimum_coins(coins, amount):
    dp = [0] + [float("inf")] * amount

    for i in range(1, amount + 1):
        for coin in coins:
            if coin <= i:
                dp[i] = min(dp[i], dp[i - coin] + 1)

    if dp[amount] == float("inf"):
        return -1

    return dp[amount]
print(minimum_coins([1, 2, 5], amount = 11))    