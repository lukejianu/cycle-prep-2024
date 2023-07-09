class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        return self.coinChangeBetter(coins, amount)

    def coinChangeBetter(self, coins: List[int], amount: int) -> int:
        # Map of amounts to minimum number of coins.
        cache = dict([(0, 0)])

        for curr_amount in range(1, amount + 1):
            minSoFar = float('inf')
            for coin in coins:
                target_amount = curr_amount - coin
                if target_amount in cache:
                    minSoFar = min(minSoFar, cache[target_amount])
            if minSoFar != float('inf'):
                cache[curr_amount] = 1 + minSoFar

        return cache.get(amount, -1)

    def coinChangeBad(self, coins: List[int], amount: int) -> int:
        coins.sort(reverse=True)
        res = self.coinChangeBadHelper(0, tuple(coins), amount)
        return -1 if res == float('inf') else res

    @cache
    def coinChangeBadHelper(self, i, coins, amount):
        n = len(coins)
        if amount == 0:
            return 0
        if amount < 0 or i >= n:
            return float('inf')
        return min(
                1 + self.coinChangeBadHelper(i, coins, amount - coins[i]),
                self.coinChangeBadHelper(i + 1, coins, amount))

