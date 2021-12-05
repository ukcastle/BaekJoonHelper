def solution():

	N = int(input())
	distances = list(map(int, input().split(' ')))
	cities = list(map(int, input().split(' ')))
	
	current_prices = cities[0]
	total = cities[0] * distances[0]
	for idx in range(1, len(cities)-1):
		if current_prices > cities[idx]:
			current_prices = cities[idx]
		total += (current_prices * distances[idx])

	print(total)