def factorial(number): #takes a number and returns the its factorial
	factorial = 1
	if number > 1:
		for each in range(1, number+1):
			factorial *= each #this multiplies each int in the range from 1 to passed number
	return factorial