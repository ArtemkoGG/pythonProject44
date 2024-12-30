def fibonacci(n):
    a, b = 0, 1
    for i in range(n):
        yield a
        a, b = b, a + b

N = 10
for number in fibonacci(N):
    print(number)
