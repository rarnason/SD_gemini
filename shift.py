import numpy as np

Ha = np.loadtxt("Ha_regions.txt",delimiter=",")
r = np.loadtxt("r_regions.txt",delimiter=",")

RAshift = []
Decshift = []

for i in range(len(Ha)):
	RAshift.append(Ha[i][0] - r[i][0])
	print RAshift[i]
	Decshift.append(Ha[i][1] - r[i][1])
	print Decshift[i] 

meanRA = np.mean(RAshift)
meandec = np.mean(Decshift)

print "Mean RA shift is " + str(meanRA)
print "Mean Dec shift is " + str(meandec)

print RAshift
print Decshift
