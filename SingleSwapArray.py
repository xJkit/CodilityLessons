#define a list can single swap to a non-descending order

P = [1, 5, 3, 3, 7]
Q = [1, 3, 3, 4, 5]
R = [1,3,5,3,4]

#check whether it's already ordered:
def isAlreadyOrdered(X):
	for i in xrange(len(X)-1):
		if X[i] > X[i+1]:
			return False
	return True

###

def getMinMRDIndex(X):
	X.reverse()
	return len(X) - X.index(min(X)) - 1


def isSingleSwapable(X):
	for i in xrange(len(X)-1):
		if X[i] > X[i+1]:
			# print "X[i] > X[i+1], i = ", i
			minMRDIndex = getMinMRDIndex( X[i+1:])
			# print "getMinMRDIndex({}) = {}".format(X[i+1:], getMinMRDIndex( X[i+1:]))			
			# print "minMRDIndex: ", minMRDIndex
			X[i], X[i+1+minMRDIndex] = X[i+1+minMRDIndex], X[i]
			#Swap done. check again:
			# print "SWAP Done: ", X
			if isAlreadyOrdered(X):
				return True
			else:
				return False

def solution(A):
	if isAlreadyOrdered(A):
		print True
	elif isSingleSwapable(A):
		print True
	else:
		print False
