class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        
        infinity = amount + 1
        arr = [infinity] * (amount + 1)
        
        arr[0] = 0
        
        for i in range(1, amount + 1):
            for coin in coins:
                if i >= coin:
                    if arr[i - coin] != infinity:
                        arr[i] = min(arr[i], arr[i - coin] + 1)

        return arr[amount] if arr[amount] != infinity else -1