class TestCase(list):

  def __init__(self):
    self.addTestCase()

  def appendTest(self,testInput,testOutput):
    self.append((testInput,testOutput))
  
  def addTestCase(self):
    testInput = ['4\r\n3\r\n0\r\n4\r\n0\r\n', '10\r\n1\r\n3\r\n5\r\n4\r\n0\r\n0\r\n7\r\n0\r\n0\r\n6\r\n']
    testOutput = ['0\r\n', '7\r\n']
    for i in range(len(testInput)):
      self.appendTest(testInput=testInput[i],testOutput=testOutput[i])


