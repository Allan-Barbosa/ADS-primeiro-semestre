print('digite "fatorial(x)" para calcular.')
def fatorial(x):
    r = 1
    y = 1
    for x in range(1, x+1):
        r = r*y
        y += 1
    return r
