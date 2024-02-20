def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

fib = fibonacci()

for _ in range(int(input("Son kiriting: "))):
    print(next(fib), end=" ")
