import sys

# 스택함수를 구현
class Stack():
	def __init__(self): # 생성자
		self.stack = []
	
	def __len__(self):
		return len(self.stack)
	
	def push(self, X : int):
		self.stack.append(X)

	def empty(self):
		if self.stack:
			return 0
		return 1

	def pop(self):
		check = self.empty()
		if check == 0: return self.stack.pop()
		return -1

	def top(self):
		check = self.empty()
		if check == 0: return self.stack[-1]
		return -1

def solution():
	# push X: 정수 X를 스택에 넣는 연산이다.
	# pop: 스택에서 가장 위에 있는 정수를 빼고, 그 수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
	# size: 스택에 들어있는 정수의 개수를 출력한다.
	# empty: 스택이 비어있으면 1, 아니면 0을 출력한다.
	# top: 스택의 가장 위에 있는 정수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
	N = int(sys.stdin.readline().rstrip())

	stack = Stack()
	for i in range(N):
		cmd = sys.stdin.readline().rstrip().split(" ")
		if cmd[0] == "push": stack.push(int(cmd[1]))
		elif cmd[0] == "pop": print(stack.pop())
		elif cmd[0] == "size": print(len(stack))
		elif cmd[0] == "empty": print(stack.empty())
		else: print(stack.top())

	# 개인회고 : 이전에 써먹었던 sys.stdin.readline().rstrip()를 input() 대신 사용하지 않으면 시간초과가 난다