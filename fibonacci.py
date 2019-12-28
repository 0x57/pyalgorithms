def fibonacci_1(n):
    a, b = 0, 1
    while b < n:
        print(b, end=' ')
        yield b
        a, b = b, a+b
    print()


def fibonacci_2(n):
    a, b = 0, 1
    if n == 0:
        return a
    if n == 1:
        return b
    return fibonacci_2(n-2) + fibonacci_2(n-1)


if __name__ == '__main__':
    print(list(fibonacci_1(10)))
    print(fibonacci_2(10))
