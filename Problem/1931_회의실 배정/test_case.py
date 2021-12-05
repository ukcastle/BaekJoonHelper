class TestCase(list):

  def __init__(self):
    self.addTestCase()

  def appendTest(self,testInput,testOutput):
    self.append((testInput,testOutput))
  
  def addTestCase(self):
    testInput = ['11\r\n1 4\r\n3 5\r\n0 6\r\n5 7\r\n3 8\r\n5 9\r\n6 10\r\n8 11\r\n8 12\r\n2 13\r\n12 14\r\n']
    testOutput = ['4\r\n']
    for i in range(len(testInput)):
      self.appendTest(testInput=testInput[i],testOutput=testOutput[i])


