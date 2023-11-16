def count_bouncy_numbers(N):
    # Initialize dp array
    dp = [[0] * 10 for _ in range(N+1)]

    # Initialize dp array for N=1
    for d in range(10):
        dp[1][d] = 1

    # Calculate dp array for N > 1
    for n in range(2, N+1):
        for d in range(10):
            for x in range(d, 10):
                dp[n][d] += dp[n-1][x]

    # Calculate total count
    count = 0
    for d in range(10):
        count += dp[N][d]

    return count

# Тестовый пример
print(count_bouncy_numbers(4)) # Output: 90

