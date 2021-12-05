class TestCase(list):

  def __init__(self):
    self.addTestCase()

  def appendTest(self,testInput,testOutput):
    self.append((testInput,testOutput))
  
  def addTestCase(self):
    testInput = ['6\r\n(())())\r\n(((()())()\r\n(()())((()))\r\n((()()(()))(((())))()\r\n()()()()(()()())()\r\n(()((())()(\r\n', '3\r\n((\r\n))\r\n())(()\r\n']
    testOutput = ['NO\r\nNO\r\nYES\r\nNO\r\nYES\r\nNO\r\n', 'NO\r\nNO\r\nNO\r\n']
    for i in range(len(testInput)):
      self.appendTest(testInput=testInput[i],testOutput=testOutput[i])


