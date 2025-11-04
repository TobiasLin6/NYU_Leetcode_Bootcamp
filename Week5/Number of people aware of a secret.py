class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        dp = [0] * (n + 1)
        
        dp[1] = 1
        
        share = 0
        
        for day in range(2, n + 1):
            if day - delay >= 1:
                share = (share + dp[day - delay]) % (10**9 + 7)
            
            if day - forget >= 1:
                share = (share - dp[day - forget] + (10**9 + 7)) % (10**9 + 7)
            
            dp[day] = share
        
        total_aware = 0
        for i in range(max(1, n - forget + 1), n + 1):
            total_aware = (total_aware + dp[i]) % (10**9 + 7)
            
        return total_aware
