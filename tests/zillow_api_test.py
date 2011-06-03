#/usr/bin/python
"""
Created on May 20, 2011

@author: ncliang
"""

import unittest
from zillowpy import zillow_api

class ZillowApiTest(unittest.TestCase):
  def setUp(self):
    self._zws_id = "X1-ZWz1bvdg36cqvf_85kuc"

  def testConstructCtorStrNoOptParams(self):
    ctor_str = zillow_api.ConstructCtorStr("GetSearchResults",
                                           ["zws_id", "address", "citystatezip"])
    self.assertEquals(ctor_str, """def _GetSearchResultsCtor(self, zws_id, address, citystatezip):
  params = {"zws-id": zws_id, "address": address, "citystatezip": citystatezip}
  base_request.BaseRequest.__init__(self, self.ConstApiUrl(), params)""")

  def testConstructCtorStrWithOptParams(self):
    ctor_str = zillow_api.ConstructCtorStr("GetChart",
                                           ["zws_id", "zpid", "unit_type"],
                                           ["width", "height", "chart_duration"])
    self.assertEquals(ctor_str, """def _GetChartCtor(self, zws_id, zpid, unit_type, width=None, height=None, chart_duration=None):
  params = {"zws-id": zws_id, "zpid": zpid, "unit-type": unit_type}
  if width:
    params["width"] = width
  if height:
    params["height"] = height
  if chart_duration:
    params["chartDuration"] = chart_duration
  base_request.BaseRequest.__init__(self, self.ConstApiUrl(), params)""")

  def testGetZestimateApiExample(self):
    gz = zillow_api.GetZestimate(self._zws_id, zpid="48749425")
    result = gz.Execute()
    self.assertEquals(result.zestimate.message.code, "0")

  def testGetSearchResultsApiExample(self):
    gsr = zillow_api.GetSearchResults(self._zws_id, address="2114 Bigelow Ave",
                                      citystatezip="Seattle, WA")
    search_result = gsr.Execute()
    self.assertEquals(int(search_result.searchresults.message.code),
                      zillow_api.GetSearchResults.REQ_SUCCESS)
    self.assertEquals(search_result.searchresults.response.results.result.zpid,
                      "48749425")

  def testGetChartApiExample(self):
    gc = zillow_api.GetChart(self._zws_id, unit_type="percent", zpid=48749425,
                             width=300, height=150)
    search_result = gc.Execute()
    self.assertEquals(int(search_result.chart.message.code), 0)

  def testGetCompsApiExample(self):
    gc = zillow_api.GetComps(self._zws_id, zpid=48749425, count=5)
    search_result = gc.Execute()
    self.assertEquals(int(search_result.comps.message.code), 0)

  def testGetDemographicsApiExample(self):
    gd = zillow_api.GetDemographics(self._zws_id, state="WA", city="Seattle",
                                    neighborhood="Ballard")
    search_result = gd.Execute()
    self.assertEquals(int(search_result.demographics.message.code), 0)
    self.assertEquals(int(search_result.demographics.response.region.id),
                      250017)

  def testGetRegionChildrenApiExampl(self):
    grc = zillow_api.GetRegionChildren(self._zws_id, state="wa", city="seattle",
                                       childtype="neighborhood")
    search_result = grc.Execute()
    self.assertEquals(int(search_result.regionchildren.message.code), 0)

  def testGetRegionChartApiExampl(self):
    grc = zillow_api.GetRegionChart(self._zws_id, city="seattle", state="WA",
                                    unit_type="percent", width=300, height=150)
    search_result = grc.Execute()
    self.assertEquals(int(search_result.regionchart.message.code), 0)


if __name__ == "__main__":
  unittest.main()
