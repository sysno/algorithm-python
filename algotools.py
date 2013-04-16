def theMostCommonItems(l, n):

	""" find the most command N items in list(l)
	"""
	i = n
	if len(l)==0 or n < 0: return 
	c = {}
	for item in l:
		c[item] = l.count(item)
	while i>0:
		(k,v) = c.items()[0]
		for m,n in c.items():
			if n>v:
				(k,v) = (m,n)
		del c[k]
		# print c
		print "%s: %d" % (k,v)
		i=i-1
