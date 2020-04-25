
# Time complexity is O(n^2)
# Space Complexity is O(1)
# def brute_buy_sell(A):
# 	max_profit = 0
# 	for i in range(len(A)):
# 		for j in range(i+1, len(A)):
# 				if A[j] - A[i] > max_profit:
# 					max_profit = A[j] - A[i]
# 	return max_profit


###################################################

# Time complexity is O(n)
# Space Complexity is O(1)
def buy_sell(A):
	profit = 0
	min_price = A[0]
	for i in range (len(A)):
		min_price = min(min_price, A[i])
		compare_price = A[i] - min_price
		profit = max(profit, compare_price)
	return profit




Array = [310, 315, 275, 295, 260, 270, 290, 230, 255, 250]
# print(brute_buy_sell(Array))
print(buy_sell(Array))
