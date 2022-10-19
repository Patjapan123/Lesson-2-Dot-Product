def dot_product(list1, list2):
	sum=0
	for i in range(len(list1)):
		japan=list1[i]*list2[i]
		sum=japan+sum
	return sum
	
pat=[1,5]
miles=[1,1]
	
print("The dot product is", dot_product(pat,miles))