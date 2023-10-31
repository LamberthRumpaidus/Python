def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        deret_fibonacci = [0, 1]
        while len(deret_fibonacci) < n:
            deret_fibonacci.append(deret_fibonacci[-1] + deret_fibonacci[-2])
        return deret_fibonacci


print(fibonacci(10))
