class TestCase(list):

  def __init__(self):
    self.addTestCase()

  def appendTest(self,testInput,testOutput):
    self.append((testInput,testOutput))
  
  def addTestCase(self):
    testInput = ['5 5\n01100\n01011\n11111\n01111\n11111\n', '5 5\n01100\n00011\n11111\n01111\n11111\n', '4 4\n0000\n0000\n0000\n0000\n', '3 6\n111000\n101111\n111111\n']
    testOutput = ['3\n', '2\n', '0\n', '2\n']
    for i in range(len(testInput)):
      self.appendTest(testInput=testInput[i],testOutput=testOutput[i])


