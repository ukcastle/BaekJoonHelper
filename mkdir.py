from src.methods import getNamespaceAndArgs, getTitleByNumber
import os
import shutil

if __name__ == '__main__':
	ns, _ = getNamespaceAndArgs()
	
	try:
		name = getTitleByNumber(ns.number)
	except:
		print(f"{ns.number}번 문제를 찾을 수 없습니다")
		exit(0)

	os.mkdir(f"./{name}")
	
	shutil.copy("./src/solution.py", f"./{name}/")
	shutil.copy("./src/test_case.py", f"./{name}/")

	print("url : ",f"https://www.acmicpc.net/problem/{ns.number}")