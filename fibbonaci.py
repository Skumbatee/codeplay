def fib(n):
	# the first fibonnaci numbers are 0 and 1
	l = [0,1]
	# loop from one to the number adding an extra interval
	for i in range(2, n+10):
		# the new fibonnaci number
		new_f = l[i-2] + l[i-1]
		if new_f <= n:
			l.append(new_f)
		else:
			break
	return l



print fib(20)