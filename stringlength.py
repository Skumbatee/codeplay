
# You are presented with two arrays, all containing positive integers. 
# One of the arrays will have one extra number, see below:
# [1,2,3] and [1,2,3,4] should return 4
# [4,66,7] and [66,77,7,4] should return 77


def string_len(string):

	alist = []
	if type(string) is list:  # use type to check if the parameter is a list
	    for item in string:
		    alist.append(len(item))

	elif type(string) is str: # use type to check if the parameter is a string
		alist.append(len(string))
	return alist

		
print string_len(['beth', 'allan']) #test case
