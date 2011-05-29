#/usr/bin/python
"""
Created on Apr 19, 2011

@author: ncliang
"""

import unittest
from zillowpy import zillow_response

class ZillowResponseTest(unittest.TestCase):
  def testResponseParsing(self):
    zresp = zillow_response.ZillowResponse("""<?xml version="1.0" encoding="utf-8"?>
<request>
  <address>1 World Way</address>
</request>""")
    zresp.request
    self.assertEquals("1 World Way", zresp.request.address)

    zresp = zillow_response.ZillowResponse("""<?xml version="1.0" encoding="utf-8"?>
<RateSummary:rateSummary xsi:schemaLocation="http://www.zillow.com/static/xsd/RateSummary.xsd /vstatic/9a7665f1f221ad96757e028b5f570e08/static/xsd/RateSummary.xsd" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:RateSummary="http://www.zillow.com/static/xsd/RateSummary.xsd">
    <request></request>
    <message>
        <text>Request successfully processed</text>
        <code>0</code>
    </message>
        <response>
            <today>
                <rate loanType="thirtyYearFixed" count="1252">5.91</rate>
                <rate loanType="fifteenYearFixed" count="839">5.68</rate>
                <rate loanType="fiveOneARM" count="685">5.49</rate>
            </today>
            <lastWeek>
                <rate loanType="thirtyYearFixed" count="8933">6.02</rate>
                <rate loanType="fifteenYearFixed" count="5801">5.94</rate>
                <rate loanType="fiveOneARM" count="3148">5.71</rate>
            </lastWeek>
        </response>
</RateSummary:rateSummary>
<!-- H:1  T:1076ms  S:630  R:Thu Sep 11 13:54:50 PDT 2008  B:3.0-comp_rel_b-SNAPSHOT -->""")
    self.assertEquals("0", zresp.rateSummary.message.code)

