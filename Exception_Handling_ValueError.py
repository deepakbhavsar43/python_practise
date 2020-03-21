try:
    value = int(input("input here :"))
except ValueError:
    print("Not appropriate value")

print("This should execute whether error arise or not...")