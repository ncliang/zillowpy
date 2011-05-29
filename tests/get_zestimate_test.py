'''
Created on May 20, 2011

@author: ncliang
'''
import unittest
from zillowpy import get_zestimate

class GetZestimateTest(unittest.TestCase):
  def setUp(self):
    self._zws_id = "X1-ZWz1bvdg36cqvf_85kuc"

  def testApiExample(self):
    gz = get_zestimate.GetZestimate(self._zws_id, "48749425")
    result = gz.Execute()
    self.assertEquals(result.zestimate.message.code, "0")


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()