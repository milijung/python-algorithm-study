n = int(input())
stairs = [0]+[int(input()) for _ in range(n)]
dp = [0] * (n+1)
dp[1] = stairs[1]

if n >= 2:  # n의 범위가 자연수임에 주의
    dp[2] = stairs[1] + stairs[2]

for i in range(3, n+1):
    dp[i] = max(dp[i-3]+stairs[i-1], dp[i-2]) + stairs[i]

print(dp[n])