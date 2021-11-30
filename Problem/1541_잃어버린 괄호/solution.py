def solution():

	inputString = input()

	split_minus = inputString.split('-')
	total = sum(list(map(int, split_minus[0].split('+'))))
	if len(split_minus) == 1:
		print(total)
	else:
		for i in range(1, len(split_minus)):
			total -= sum(list(map(int, split_minus[i].split('+'))))
		print(total)