def firstAlphabet(s):
		# code here
		l=s.split(" ")
		op=""
		for i in l:
		    op+=i[0]
		return op

print(firstAlphabet("Nikhil is a don"))