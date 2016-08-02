def f(x):
    import math
    return 10*math.e**(math.log(0.5)/5.27 * x)


def radiationExposure(start, stop, step):
    i = start
    customRange = []
    while i < stop:
        customRange.append(i)
        i += step
    r = 0
    for x in customRange:
        r += f(x)
    return r


print radiationExposure(0, 5, 1) - 39.10318784326239
print radiationExposure(5, 11, 1) - 22.94241041057671
print radiationExposure(0, 11, 1) - 62.0455982538
print radiationExposure(40, 100, 1.5) - 0.434612356115
