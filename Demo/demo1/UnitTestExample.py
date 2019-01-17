from HtmlTestRunner import HTMLTestRunner
import unittest
# import sys
# import os
# sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from demo1 import Examples


Example = Examples.Example



class Test(unittest.TestCase):

    def setUp(self):
        print ("Running before test")
#         unittest.TestCase.setUp(self)
        
    def tearDown(self):
#         unittest.TestCase.tearDown(self)
        print ("Runnig after test")
    def test_add(self):
        #result = Example.add(self, 10, 20)
        self.assertEqual(Example.add(self, 10, 20),30)
        self.assertEqual(Example.add(self, 1, 2),3)
        self.assertEqual(Example.add(self, 0, 0),0)
        self.assertEqual(Example.add(self, -10, 20),10)
        self.assertEqual(Example.add(self, -10, -20),-30)
        

 
if __name__ == '__main__':
    #import sys;sys.argv = ['', 'Test.testName']

    unittest.main(testRunner=HTMLTestRunner(output='D:/Desktop/Workspaces/EclipsePhoton2Workspace/Demo/reports'))