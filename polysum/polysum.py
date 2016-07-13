import math

def polysum(n,s):
	area = (.25*n*(s**2))/math.tan(math.pi/n)
	perimeter = n*s
	return round(area + (perimeter ** 2), 4)

print polysum(3,5) - 235.8253
print polysum(96,68) - 46004750.1144