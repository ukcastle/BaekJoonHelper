class TestCase(list):

  def __init__(self):
    self.addTestCase()

  def appendTest(self,testInput,testOutput):
    self.append((testInput,testOutput))
  
  def addTestCase(self):
    testInput = """
    1 2
    """
    testOutput = """
    3
    """
    self.appendTest(testInput=testInput,testOutput=testOutput)


