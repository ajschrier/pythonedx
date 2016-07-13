def iterPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''
    i = 1
    while exp > 0:
    	i *= base
    	exp -= 1
    return i

# print iterPower(3,3)

