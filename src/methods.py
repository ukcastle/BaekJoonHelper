import os
import re
from datetime import datetime
import argparse
from urllib.request import urlopen
from bs4 import BeautifulSoup

def getFileName(questionNum):
	folderName = [x for x in os.listdir('./Problem') if re.findall(rf"^{questionNum}_",x)]

	if len(folderName) == 1:
		return 'Problem.' + folderName[0]
	
	for name in folderName:
		print(f"검색된 폴더 이름 : {name}")

	raise "폴더를 다시 확인해주세요 (검색 조건: 문제번호_~~~~~)"

def calcTime_decorator(realFunc):
	def func(*args, **kwargs):
		t = datetime.now()
		realFunc(*args, **kwargs)
		print(f"running time = {datetime.now()-t}")
	return func


def refineString(strs):
	if isinstance(strs, str):
		ret = [x.strip() for x in strs.strip().split("\n") if re.search("\S", x)]
	else:
		ret = str(strs)
	return ret


def getNamespaceAndArgs():
	parser = argparse.ArgumentParser()
	parser.add_argument('number', type=int, help='Input Question Number')
	parser.add_argument('--test', help="If you want only print", action="store_true")
	ns, args = parser.parse_known_args()

	return ns, [parser.prog] + args

def getTitleByNumber(number):
	html = urlopen(f"https://www.acmicpc.net/problem/{number}")
	bsObject = BeautifulSoup(html, "html.parser")
	return bsObject.head.findAll("title")[0].__str__()[7:-8].replace("번: ","_")

def getProblem(number):
	html = urlopen(f"https://www.acmicpc.net/problem/{number}")
	bsObject = BeautifulSoup(html, "html.parser")

	# 문제 가져오기
	# problem_description = bsObject.select('#problem_description > p, #problem_description > pre, #problem_description > img, #problem_description > blockquote, #problem_description > table, #problem_description > ol, #problem_description > ul, #problem_description > li')
	# 문제의 경우, 다양한 태그가 포함되어 있음
	problem_description = bsObject.select('#problem_description')

	# 이 외, 문자만 존재하므로 특정태그만 가져와도 됨
	input_description = bsObject.select('#problem_input > p')
	output_description = bsObject.select('#problem_output > p')
	sample_i = bsObject.select("pre[id^=sample-input]")
	sample_o = bsObject.select("pre[id^=sample-output]")

	return problem_description, input_description, output_description, sample_i, sample_o