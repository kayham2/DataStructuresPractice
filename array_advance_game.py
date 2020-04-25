def array_advance_game(array):
	reach = []
	furthest_reached = 0
	for i in range(0,len(array)):
		if i > furthest_reached:
			return False
		reach.append(array[i]+i)
		furthest_reached = max(reach)
		if furthest_reached >= len(array)-1:
			return True
		

A1 = [3,3,1,0,2,0,1]
# print(array_advance_game(A1))

A2 = [3,2,0,0,2,0,1]
print(array_advance_game(A2))