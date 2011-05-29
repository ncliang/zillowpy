#/usr/bin/python
"""
Created on May 20, 2011

@author: ncliang
"""

class ZillowInterface(object):
  def __init__(self, api_name, req_params, opt_params=[]):
    self.api_name = api_name
    self.req_params = req_params
    self.opt_params = opt_params


ZILLOW_API_INTERFACE = [
    # Home Valuation API
    ZillowInterface("GetSearchResults", ["zws_id", "address", "citystatezip"]),
    ZillowInterface("GetZestimate", ["zws_id", "zpid"]),
    ZillowInterface("GetChart", ["zws_id", "zpid", "unit_type"],
                    ["width", "height", "chart_duration"]),
    ZillowInterface("GetComps", ["zws_id", "zpid", "count"]),

    # Neighborhood Information
    ZillowInterface("GetDemographics", ["zws_id"],
                    ["regionid", "state", "city", "neighborhood", "zip"]),
    ZillowInterface("GetRegionChildren", ["zws_id"],
                    ["regionId", "state", "county", "city", "childtype"]),
    ZillowInterface("GetRegionChart", ["zws_id", "unit_type"],
                    ["city", "state", "neighborhood", "zip", "width", "height",
                     "chart_duration"]),

    # Mortgage API
    ZillowInterface("GetRateSummary", ["zws_id"],
                    ["state", "output", "callback"]),
    ZillowInterface("GetMonthlyPayments", ["zws_id", "price"],
                    ["down", "dollarsdown", "zip", "output", "callback"]),

    # Property Details API
    ZillowInterface("GetDeepSearchResults", ["zws_id", "address", "citystatezip"]),
    ZillowInterface("GetDeepComps", ["zws_id", "zpid", "count"]),
    ZillowInterface("GetUpdatedPropertyDetails", ["zws_id", "zpid"]),

    # Postings API
    ZillowInterface("GetRegionPostings", ["zws_id"],
                    ["zipcode", "citystatezip", "rental", "posting_type"])
]