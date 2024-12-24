import time
def catalan_iterative(n):
    dp = [0] * (n + 1)
    dp[0] = 1

    for i in range(1, n + 1):
        for j in range(i):
            dp[i] += dp[j] * dp[i - j - 1]
    return dp[n]
start_time = time.time()
result = catalan_iterative(0)
end_time = time.time()

print(f'Output: {result}') 
print(f'Waktu eksekusi: {end_time - start_time} detik')
