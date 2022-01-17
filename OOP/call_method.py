class Multiplier:
    def __call__(self, x, y):
        return x*y

multiply = Multiplier()
print(multiply(19, 19)) # 361
# то же самое
print(multiply.__call__(19, 19)) # 361