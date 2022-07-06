

def exponentiate(x, y):
    """return x to the power of y"""
    return x ** y


def raise_to_fourth_power(x):
    """raises to the 4th power"""
    return exponentiate(x, 4)

square = lambda x: exponentiate(x, 2)

cube = lambda x: exponentiate(x, 3)

print(square(2))
print(cube(2))
print(raise_to_fourth_power(2))



