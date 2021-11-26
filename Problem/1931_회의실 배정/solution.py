def solution():

	# 회의의 개수
	N = int(input())

	Meet_lst = []
	for i in range(N):
		Meet_lst.append(list(map(int, input().split(' '))))

	Meet_lst = sorted(Meet_lst, key=lambda x: (x[1], x[0]))

	Count = 1
	End = Meet_lst[0][1]
	for i in range(1, len(Meet_lst)):
		s, e = Meet_lst[i]
		if s >= End:
			Count += 1
			End = e
	print(Count)