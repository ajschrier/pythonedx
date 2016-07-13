def f(x):
    import math
    return 10*math.e**(math.log(0.5)/5.27 * x)


def radiationExposure(start, stop, step):
    '''
    Computes and returns the amount of radiation exposed
    to between the start and stop times. Calls the 
    function f (defined for you in the grading script)
    to obtain the value of the function at any point.
 
    start: integer, the time at which exposure begins
    stop: integer, the time at which exposure ends
    step: float, the width of each rectangle. You can assume that
      the step size will always partition the space evenly.

    returns: float, the amount of radiation exposed to 
      between start and stop times.
    '''
    i = float(start)
    customRange = []
    while i < stop:
        customRange.append(i)
        i += step
    r = 0.0
    for x in customRange:
        r += f(x) * step
        print '{}: {}'.format(x,r)
    print '------'
    return r


test1 = radiationExposure(0,5,1) - 39.10318784326239
test2 = radiationExposure(5,11,1) - 22.94241041057671
test3 = radiationExposure(0,11,1) - 62.0455982538
test4 = radiationExposure(40,100,1.5) - 0.434612356115

tests = [test1, test2, test3, test4]
for test in tests:
    print test
    if abs(test) < 0.01:
        print "Within threshold"
    else:
        print "Outside threshold"
    print

# print f(5)
# print f(0)