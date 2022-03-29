def recurse(n):
    if n == 0:
        return 0
    else:
        return n + recurse(n-1)


print(recurse(5))