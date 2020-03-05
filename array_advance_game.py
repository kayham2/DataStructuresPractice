array1 = [3,2,0,0,2,0,1]
counter = 0
furthest_reached = []

for number in array1:
	furthest_reached.append(counter + number)  
	counter += 1
	if counter > max(furthest_reached):
		break

print(furthest_reached, counter)
if max(furthest_reached) <= len(array1)-1:
	print("Not possible")
else:
	print("We're good!")
