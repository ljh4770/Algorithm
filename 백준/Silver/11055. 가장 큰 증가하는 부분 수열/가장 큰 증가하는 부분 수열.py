import sys
input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split(' ')))
dp = [v for v in arr]

for i in range(n):
    for j in range(i):
        if arr[j] < arr[i]:
            dp[i] = max(dp[i], dp[j] + arr[i])
print(max(dp))