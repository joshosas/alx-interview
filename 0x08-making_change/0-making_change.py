#!/usr/bin/python3
"""Change making module.
"""


def makeChange(coins, total):
    """implement a function called makeChange
       that takes two parameters:coins and total.
       The function should return the fewest number
       of coins needed to meet the total amount.
    """
    if total <= 0:
        return 0

    # Create a table to store the min no. of coins required
    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    # Iterate through each coin value
    for coin in coins:
        # Iterate from coin value to total
        for amount in range(coin, total + 1):
            # Check if using the current coin
            # requires fewer coins than the current value in the table
            if dp[amount - coin] + 1 < dp[amount]:
                dp[amount] = dp[amount - coin] + 1

    # Check if the total amount can be met
    if dp[total] == float('inf'):
        return -1
    else:
        return dp[total]
