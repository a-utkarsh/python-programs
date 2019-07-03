A=[-2,1,-3,4,-1,2,1,-5,4]
best = -1000000000000
sumsofar = 0
for x in A:
    sumsofar =sumsofar+ x
    #print(sumsofar,"S1", end=" ")
    best = max(sumsofar, best)
    #print(best,end=" ")
	# Doing this last, to handle case
	# when all numbers are negative.
    sumsofar = max(sumsofar, 0)
    #print(sumsofar,"S2 ",end=" ")
#print(sumsofar)
print(best)