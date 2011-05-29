#/usr/bin/python
"""
Created on Apr 19, 2011

@author: ncliang
"""

import unittest
from zillowpy import get_search_results

class GetSearchResultsTest(unittest.TestCase):
  def setUp(self):
    self._zws_id = "X1-ZWz1bvdg36cqvf_85kuc"
  
  def testNoExactMatchFound(self):
    gsr = get_search_results.GetSearchResults(self._zws_id, "1 World Way",
                                              "Los Angeles, CA")
    search_result = gsr.Execute()
    self.assertEquals(int(search_result.searchresults.message.code),
                      get_search_results.GetSearchResults.NO_EXACT_MATCH)

  def testApiExample(self):
    gsr = get_search_results.GetSearchResults(self._zws_id, "2114 Bigelow Ave",
                                              "Seattle, WA")
    search_result = gsr.Execute()
    self.assertEquals(int(search_result.searchresults.message.code),
                      get_search_results.GetSearchResults.REQ_SUCCESS)
    self.assertEquals(search_result.searchresults.response.results.result.zpid,
                      "48749425")


if __name__ == "__main__":
    unittest.main()