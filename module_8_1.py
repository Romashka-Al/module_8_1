def add_everything_up(a, b):
    try:
        return a + b
    except TypeError:
        if type(a) == str or type(b) == str:
            return str(a) + str(b)
        return float(a) + float(b)


print(add_everything_up(993, 'zxc'))
print(add_everything_up(19.26, 228))
print(add_everything_up('Коломбина C', 6))
