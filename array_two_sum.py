# Array A is a sorted array
# Values in array must sum up to target
# We may only use the element once

# Time complexity is O(n^2)
# Space Complexity is O(1)
def brute_two_sum(A, x):
	pairs = list()
	for i in A:
		for j in A[1+i:]:
			if i + j == x:
				print(i, j)
				return True
	return pairs, y

###############################################

# Time complexity is O(n)
# Space Complexity is O(n) - we need n hashtable items
def two_sum_hash_table(A, x):
	ht = dict()
	for i in range(len(A)):
		if A[i] in ht:
			print(ht[A[i]], A[i])
			return True
		else:
			ht[x - A[i]] = A[i]

	return False

###############################################

# Time complexity is O(n)
# Space Complexity is O(1)
def two_sum(A, x):
	index = len(A)-1
	p = 0

	while p <= index:
		y = A[p] + A[index]
		if y == x:
			print(A[p], A[index]) 
			return True
		elif y < x:
			p +=1
		else:
			index -=1
	return False



Array = [-2, 1, 2, 4, 7, 11]
target = 13
# print(brute_two_sum(Array, target))
# print(two_sum_hash_table(Array, target))
print(two_sum(Array, target))






