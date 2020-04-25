# MY METHOD
# def arb_prec_increment(array):
# 	index = len(array) -1 
# 	carry = 0 
# 	while index >= 0:
# 		if index == len(array)-1:
# 			x = array[index] + 1 + carry
# 		else: 
# 			x = array[index] + carry
		
# 		if x >= 10:
# 			carry = 1
# 			array[index] = x%10
# 		else:
# 			carry = 0
# 			array[index] = x
# 		index -= 1

# 	if carry == 1:
# 		array = [1] + array
# 	return array

# A = [9,9,9]
# print(arb_prec_increment(A))


# THEIR METHOD
# or
# s = ''.join(map(str, A))
# print(int(s)+1)

def plus_one(A):
	A[-1] += 1

	for i in range(len(A)-1, 0, -1):
		if A[i] == 10:
			A[i] = 0
			A[i-1] +=1
	if A[0]==10:
		A[0] = 1
		A.append(0)
	return A


Array1 = [9, 9, 9]
print(plus_one(Array1))