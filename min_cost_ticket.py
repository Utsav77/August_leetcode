class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        #dp[i] = min(dp[i+1]+costs[0],dp[i+7]+costs[1],dp[i+30]+costs[2])
        
        dayset = set(days)
        
        dp = [0]*366
        
        for i in range(len(dp)):
            if i in dayset:
                dp[i] = min(dp[i-1]+costs[0], dp[i-7]+costs[1],dp[i-30]+costs[2])
            else:
                dp[i] = dp[i-1]
        return dp[-1]
 