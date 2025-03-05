# def fibonacci(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     return fibonacci(n - 1) + fibonacci(n - 2)

# print(fibonacci(10))

# 메모이제이션을 활용해 개선된 버전
def fibonacci_memo(n, memo={}):
    if n in memo:
        return memo[n]
    if n == 0:
        return 0
    elif n == 1:
        return 1
    memo[n] = fibonacci_memo(n - 1, memo) + fibonacci_memo(n - 2, memo)
    return memo[n]

# 테스트
print(fibonacci_memo(10))  # 빠르게 결과 출력 가능!
