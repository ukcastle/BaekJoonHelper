class TestCase(list):

  def __init__(self):
    self.addTestCase()

  def appendTest(self,testInput,testOutput):
    self.append((testInput,testOutput))
  
  def addTestCase(self):
    testInput = ['3\r\n0 0 13 40 0 37\r\n0 0 3 0 7 4\r\n1 1 1 1 1 5\r\n']
    testOutput = ['2\r\n1\r\n0\r\n']
    for i in range(len(testInput)):
      self.appendTest(testInput=testInput[i],testOutput=testOutput[i])


