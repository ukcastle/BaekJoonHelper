class TestCase(list):

  def __init__(self):
    self.addTestCase()

  def appendTest(self,testInput,testOutput):
    self.append((testInput,testOutput))
  
  def addTestCase(self):
    testInput = ['5 6\r\n3 2 1 2\r\n2 3 3 4 4 5\r\n', '7 5\r\n1 1 1 1 1 1\r\n4 5 6 6 7\r\n', '6 4\r\n2 3 5 8 10\r\n1 3 3 4\r\n']
    testOutput = ['8\r\n', '4\r\n', 'F\r\n']
    for i in range(len(testInput)):
      self.appendTest(testInput=testInput[i],testOutput=testOutput[i])


