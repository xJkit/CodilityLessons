# shift array A to the right by K elements.

A = [3,4,2]
K = 3

def solution(A1, K1):
	print "A: ", A1
	print "K: ", K1
	for i in xrange(K1):
		popElement = A.pop()
		# print "pop out: ", popElement
		A.insert(0, popElement)
	# print "A': ", A
	return A
print solution(A, K)


### Grade: 87%###
"""
1. empty array failed.
	IndexError: pop from empty list
"""
