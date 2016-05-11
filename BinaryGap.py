# Binary Gaps
def solution(N):
	A = N #Original No.
	Digit = []

	def findMaxDigit(A):
		MLD = 0
		while A >= 2**MLD:
			MLD += 1
		return MLD-1
	Digit.append(findMaxDigit(A))
	def findDigit(A):
		B = A - 2**Digit[0]
		for i in xrange(Digit[0]-1, -1, -1):
			while B >= 2**i:
				Digit.append(i)
				B -= 2**i
		#B should == 0
		print "B: ", B
	findDigit(A)
	print "A: ", A
	print Digit
	print "ANS: ", bin(A)

	def findMaxBinaryGap(Digit):
		mbg = 0
		for i in xrange(len(Digit)-1):
			d = Digit[i]-Digit[i+1]
			mbg = max(mbg, d)
		return mbg-1
	print "MBG: ", findMaxBinaryGap(Digit)
solution(1024)