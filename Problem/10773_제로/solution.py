import sys

def solution():
	N = int(sys.stdin.readline().rstrip())

	stack = list()
	for i in range(N):
		num = int(sys.stdin.readline().rstrip())
		if num == 0: stack.pop()
		else: stack.append(num)
	
	print(sum(stack))