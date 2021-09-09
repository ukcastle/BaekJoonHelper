from unittest.mock import patch
import unittest
from io import StringIO
from importlib import import_module

from src.methods import getFileName,calcTime_decorator, refineString, getNamespaceAndArgs

class Test(unittest.TestCase):

	fileName = ""
	isTest = False

	def setUp(self) -> None:
			self.testList = getattr(import_module(f"{self.fileName}.test_case"),"TestCase")()
			self.solution = getattr(import_module(f"{self.fileName}.solution"), "solution")	
			return super().setUp()

	def testSolution(self):
		print()
		for testInput, answer in self.testList:
			testInput = refineString(testInput)
			answer = refineString(answer)

			self._testSolution(testInput, answer)

	@calcTime_decorator
	def _testSolution(self ,testInput, rightAnswer):
		with patch('sys.stdout', new = StringIO()) as fake_out:
			with patch('builtins.input',side_effect=testInput):
				self.solution()
				printValue = fake_out.getvalue()
				if not self.isTest:
					self.assertEqual(printValue, "\n".join(str(x) for x in rightAnswer)+"\n")
		userAnswer = printValue.split("\n")[:-1]
		print(f"userAns={userAnswer}, rightAnswer={rightAnswer}", end="\t")


if __name__ == '__main__':
	ns, otherArg = getNamespaceAndArgs()

	Test.fileName = getFileName(ns.number)
	Test.isTest = ns.test
	try:
		unittest.main(argv=otherArg)

	finally:
		print(f"https://www.acmicpc.net/problem/{ns.number}")