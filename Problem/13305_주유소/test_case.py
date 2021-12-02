class TestCase(list):

  def __init__(self):
    self.addTestCase()

  def appendTest(self,testInput,testOutput):
    self.append((testInput,testOutput))
  
  def addTestCase(self):
    testInput = ['4\r\n2 3 1\r\n5 2 4 1\r\n', '4\r\n3 3 4\r\n1 1 1 1\r\n']
    testOutput = ['18\r\n', '10\r\n']
    for i in range(len(testInput)):
      self.appendTest(testInput=testInput[i],testOutput=testOutput[i])


