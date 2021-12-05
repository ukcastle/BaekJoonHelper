def solution():

	N = int(input())
	time_lst = list(map(int, input().split()))
	time_lst.sort()

	total = 0
	while len(time_lst) != 0:
		total += sum(time_lst)
		time_lst.pop()
	
	print(total)