class TestCase(list):

  def __init__(self):
    self.addTestCase()

  def appendTest(self,testInput,testOutput):
    self.append((testInput,testOutput))
  
  def addTestCase(self):
    testInput = ['5 5\r\n01100\r\n01011\r\n11111\r\n01111\r\n11111\r\n', '5 5\r\n01100\r\n00011\r\n11111\r\n01111\r\n11111\r\n', '4 4\r\n0000\r\n0000\r\n0000\r\n0000\r\n', '3 6\r\n111000\r\n101111\r\n111111\r\n']
    testOutput = ['3\r\n', '2\r\n', '0\r\n', '2\r\n']
    for i in range(len(testInput)):
      self.appendTest(testInput=testInput[i],testOutput=testOutput[i])


