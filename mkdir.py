from src.methods import getNamespaceAndArgs, getTitleByNumber, getProblem
import os
import shutil

if __name__ == '__main__':
	ns, _ = getNamespaceAndArgs()
	
	try:
		name = getTitleByNumber(ns.number)
		problem_description, input_description, output_description, sample_i, sample_o = getProblem(ns.number)
	except:
		print(f"{ns.number}번 문제를 찾을 수 없습니다")
		exit(0)

	os.mkdir(f"./Problem/{name}")
	
	shutil.copy("./src/solution.py", f"./Problem/{name}/")
	# shutil.copy("./src/test_case.py", f"./Problem/{name}/")
	
	inputs = []
	outputs = []
	
	# readme.md 파일 생성
	f = open(f"./Problem/{name}/README.md", 'w', encoding='utf-8')
	f.write('### 문제\n')
	f.write('\n'.join([str(i).replace("src=\"", "src=\"https://www.acmicpc.net/") for i in problem_description]))
	f.write('\n<hr/>\n\n')
	f.write('### 입력\n')
	f.write('\n'.join([str(i) for i in input_description]))
	f.write('\n<hr/>\n\n')
	f.write('### 출력\n')
	f.write('\n'.join([str(i) for i in output_description]))
	f.write('\n<hr/>\n\n')
	for i in range(len(sample_i)):
		f.write('### 입력 예시 {}\n'.format(i+1))
		f.write(sample_i[i].text.replace('\n', '\r\n') + '\n')
		inputs.append(sample_i[i].text.replace('\n', '\r\n'))
		f.write('### 출력 예시 {}\n'.format(i+1))
		f.write(sample_o[i].text.replace('\n', '\r\n') + '\n<hr/>\n\n')
		outputs.append(sample_o[i].text.replace('\n', '\r\n'))
	f.close()
	
	# test_case 수정
	f = open("./src/test_case.py", 'r', encoding='utf-8')
	py_file = f.read()
	f.close()

	# 수정
	py_file = py_file.replace("\"input_modify\"", str(inputs))
	py_file = py_file.replace("\"output_modify\"", str(outputs))
	
	# 작성
	f = open(f"./Problem/{name}/test_case.py", 'w', encoding='utf-8')
	f.write(py_file)
	f.close()

	print("url : ",f"https://www.acmicpc.net/problem/{ns.number}")