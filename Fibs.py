#Fibs
fibs = [0,1]
numZS = input("How many Fibonacci numbers do you want?")
for i in range(numZS-2):
    fibs.append(fibs[-2] + fibs[-1])

print fibs
