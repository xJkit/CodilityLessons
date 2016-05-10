from math import ceil
from math import floor

def wholeSquareNumber(A, B):
	
	if (A < 0) & (B < 0):
		return 0
	elif (A <= 0 ) & (B == 0):
		return 1
	elif (A <= 0 ) & (B > 0):
		sqrB = B**0.5
		B_end = int(floor(sqrB))
		return B_end + 1
	elif (A == 0) & (B == 0):
		return 1
	elif (A > 0) & (B > 0):
		sqrA = A**0.5
		sqrB = B**0.5
		A_start = int(ceil(sqrA))
		B_end = int(floor(sqrB))
		return B_end - A_start + 1

print wholeSquareNumber(5000,10000)