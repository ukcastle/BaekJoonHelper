class TestCase(list):

  def __init__(self):
    self.addTestCase()

  def appendTest(self,testInput,testOutput):
    self.append((testInput,testOutput))
  
  def addTestCase(self):
    testInput = ['55-50+40\r\n', '10+20+30+40\r\n', '00009-00009\r\n']
    testOutput = ['-35\r\n', '100\r\n', '0\r\n']
    for i in range(len(testInput)):
      self.appendTest(testInput=testInput[i],testOutput=testOutput[i])


