import copy

def insert_sort(l):

	if len(l)==0: pass
	for j in range(1,len(l)):

		key = l[j]
		i = j-1
		while ( i>=0 and l[i]>key ):
			l[i+1] = l[i]
			l[i] = key
			i=i-1

def selection_sort(l):
	
	for j in range(0, len(l)-1):
		idex = j 
		i = j+1
		while ( i<=len(l) -1):
			if l[i] < l[idex]: idex = i
			i = i+1

		if j != idex: 
			t = l[idex]
			l[idex] = l[j]
			l[j] = t


def merge_sort(l,p,r):
	if (p<r):
		q = (r+p)/2
		merge_sort(l,p,q)
		merge_sort(l,q+1,r)
		merge(l,p,q,r)

def merge(l,p,q,r):
	L1 = copy.deepcopy(l[p:(q+1)])
	L2 = copy.deepcopy(l[(q+1):(r+1)])	

	L1.append(999999)
	L2.append(999999)
	i = 0
	j = 0
	for k in range(p,r+1):
		if(L1[i] < L2[j]): 
			l[k] = L1[i]
			i = i + 1
		else:
			l[k] = L2[j]
			j = j + 1








