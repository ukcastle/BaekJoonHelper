class TestCase(list):

  def __init__(self):
    self.addTestCase()

  def appendTest(self,testInput,testOutput):
    self.append((testInput,testOutput))
  
  def addTestCase(self):
    testInput = ['5\r\n1 2 3 4 5\r\n2\r\n1 1\r\n1 5\r\n', '6\r\n4 5 6 1 2 3\r\n3\r\n1 3\r\n2 4\r\n1 6\r\n', '6\r\n3 4 5 6 1 2\r\n3\r\n1 4\r\n6 6\r\n1 6\r\n']
    testOutput = ['1\r\n1\r\n', '1\r\n2\r\n2\r\n', '1\r\n1\r\n2\r\n']
    for i in range(len(testInput)):
      self.appendTest(testInput=testInput[i],testOutput=testOutput[i])


