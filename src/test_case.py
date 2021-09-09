class TestCase(list):

  def __init__(self):
    self.addTestCase()

  def appendTest(self,testInput,testOutput):
    self.append((testInput,testOutput))
  
  def addTestCase(self):
    testInput = """
    echo me
    """
    testOutput = """
    echo me
    """
    self.appendTest(testInput=testInput,testOutput=testOutput)


