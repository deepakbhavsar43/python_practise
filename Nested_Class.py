class outer:
    def __init__(self):
        print("Outer constructor.")
        self.inner()

    class inner:
        def __init__(self):
            print("Inner constructor.")

obj1=outer()
# obj2=inner()