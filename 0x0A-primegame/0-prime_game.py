#!/usr/bin/python3
"""Prime game module.
"""


def isWinner(x, nums):
    """Determines the winner of a prime game session with `x` rounds.
    """
    if x < 1 or not nums:
        return None
    Maria_wins, Ben_wins = 0, 0

    n = max(nums)
    prime_numbers = [True for _ in range(1, n + 1, 1)]
    prime_numbers[0] = False
    for i, is_prime in enumerate(prime_numbers, 1):
        if i == 1 or not is_prime:
            continue
        for j in range(i + i, n + 1, i):
            prime_numbers[j - 1] = False

    for _, n in zip(range(x), nums):
        prime_nums_count = len(list(filter(lambda x: x, prime_numbers[0: n])))
        Ben_wins += prime_nums_count % 2 == 0
        Maria_wins += prime_nums_count % 2 == 1
    if Maria_wins == Ben_wins:
        return None
    return 'Maria' if Maria_wins > Ben_wins else 'Ben'
