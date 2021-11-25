class TestCase(list):

  def __init__(self):
    self.addTestCase()

  def appendTest(self,testInput,testOutput):
    self.append((testInput,testOutput))
  
  def addTestCase(self):
    testInput = ['3\r\n022\r\n101\r\n110\r\n', '2\r\n01\r\n10\r\n', '5\r\n01231\r\n00231\r\n00031\r\n00002\r\n00000\r\n', '5\r\n15555\r\n11111\r\n15111\r\n11111\r\n11111\r\n', '10\r\n0100000000\r\n0020000000\r\n0003000000\r\n0000400000\r\n0000050000\r\n0000006000\r\n0000000700\r\n0000000080\r\n0000000009\r\n1111111111\r\n']
    testOutput = ['2\r\n', '2\r\n', '4\r\n', '3\r\n', '10\r\n']
    for i in range(len(testInput)):
      self.appendTest(testInput=testInput[i],testOutput=testOutput[i])


