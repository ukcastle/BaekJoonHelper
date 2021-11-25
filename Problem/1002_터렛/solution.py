import math

def solution():
	n = int(input())
	# 류재명이 있을 수 있는 위치는 사정거리가 겹치는 곳임
	for i in range(n):
		x1, y1, r1, x2, y2, r2 = list(map(int, input().split()))
		d = math.sqrt((x2-x1)**2 + (y2-y1)**2) # 터렛간의 거리
		
		# 터렛 겹치기
		if d == 0:
			if r1 == r2: # 사정거리가 같을 경우
				print(-1)
			else: # 사정거리가 다를 경우
				print(0)
		
		else: # 터렛 못겹침
			if d == r1 + r2 or abs(r1 - r2) == d: # 한점에서 만남
				print(1)
			elif abs(r1 - r2) < d < r1 + r2: # 2점에서 만남
				print(2)
			else: # 사정거리가 겹치지 않음
				print(0)