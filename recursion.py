def replicate_iter(n, p):
	x=list()
	if p == []:
		raise ValueError
	if n == [] or n == str(n):
		raise ValueError
	while n>0:
		x.append(p)
		n=n-1
	return x
	



def replicate_recur(n, p):
	if p == []:
		raise ValueError
	if n == [] or n == str(n):
		raise ValueError
	if n<=0:
		return []
	else:
		return [p] + replicate_recur(n-1, p)
	
			
			
print replicate_iter(6, 4)
