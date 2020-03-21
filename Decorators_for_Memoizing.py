def memoize(func):
    cache = {}

    def wrapper(*args, **kwargs):
        print(cache)

        if args not in cache:
            print(f"Caching NEW value for {func.__name__}{args}")
            cache[args]=func(*args)
        else:
            print(f"Using OLD value for {func.__name__}{args}")
        return cache[args]
    return wrapper

@memoize
def add(x, y):
    print("Running add!")
    return x+y

@memoize
def sub(x, y):
    print("Running sub!")
    return x-y

print(add(1, 2))
print(sub(2, 3))
print(add(1, 2))
print(sub(2, 3))
print(add(3, 4))
print(sub(4, 5))
print(add(5, 6))
print(sub(6, 7))