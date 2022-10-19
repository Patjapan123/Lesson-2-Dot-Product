import code

if code.dot_product([1,3,5],[2,4,6]) == 44:
	print("Test Case 1 Passed!")
else:
	print("Test Case 1 Failed! [1,3,5],[2,4,6] expected 44, got", code.dot_product([1,3,5],[2,4,6]))

if code.dot_product([1,-2],[1,1]) == -1:
	print("Test Case 2 Passed!")
else:
	print("Test Case 2 Failed! [1,-2],[1,1] expected -1, got", code.dot_product([1,-2],[1,1]))