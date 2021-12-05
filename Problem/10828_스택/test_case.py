class TestCase(list):

  def __init__(self):
    self.addTestCase()

  def appendTest(self,testInput,testOutput):
    self.append((testInput,testOutput))
  
  def addTestCase(self):
    testInput = ['14\r\npush 1\r\npush 2\r\ntop\r\nsize\r\nempty\r\npop\r\npop\r\npop\r\nsize\r\nempty\r\npop\r\npush 3\r\nempty\r\ntop\r\n', '7\r\npop\r\ntop\r\npush 123\r\ntop\r\npop\r\ntop\r\npop\r\n']
    testOutput = ['2\r\n2\r\n0\r\n2\r\n1\r\n-1\r\n0\r\n1\r\n-1\r\n0\r\n3\r\n', '-1\r\n-1\r\n123\r\n123\r\n-1\r\n-1\r\n']
    for i in range(len(testInput)):
      self.appendTest(testInput=testInput[i],testOutput=testOutput[i])


