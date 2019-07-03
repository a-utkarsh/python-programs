def canCompleteCircuit(gas, cost):
	if sum(gas) < sum(cost): return -1
	n, s, r = len(gas), 0, 0
	for i in range(n):
		if gas[i] + r < cost[i]:
			s, r = i+1, 0
		else:
			r += gas[i]-cost[i]
	return s
