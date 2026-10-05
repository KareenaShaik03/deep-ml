import math

def calculate_eigenvalues(matrix: list[list[float|int]]) -> list[float]:
	a,b = matrix[0]
	c,d = matrix[1]

	A = 1
	B = -(a+d)
	C = a*d - b*c

	discrimination = B**2 - 4*A*C 

	eigenvalue1 = (-B + math.sqrt(discrimination))/(2*A)
	eigenvalue2 = (-B - math.sqrt(discrimination))/(2*A)
	 
	eigenvalues = sorted([eigenvalue1,eigenvalue2], reverse = True)

	return eigenvalues