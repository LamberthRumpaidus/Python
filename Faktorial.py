def faktorial(n):
    if n == 0:
        return 1
    else:
        return faktorial(n-1) * n


print(faktorial(10))
