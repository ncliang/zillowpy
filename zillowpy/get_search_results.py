#/usr/bin/python
"""
Created on Apr 19, 2011

@author: ncliang
"""

from zillowpy import base_request


class GetSearchResults(base_request.BaseRequest):
  """classdocs"""

  INVALID_OR_MISSING_ADDRESS = 500
  INVALID_OR_MISSING_CITYSTATE_ZIP = 501
  NO_RESULTS = 502
  FAILED_TO_RESOLVE = 503
  NO_COVERAGE_FOR_AREA = 504
  TIMEOUT = 505
  ADDR_STR_TOO_LONG = 506
#  NO_EXACT_MATCH = 507
  NO_EXACT_MATCH = 508  # Docs say 507, but reality says 508

  def __init__(self, zws_id, address, citystatezip):
    """Constructor"""
    base_request.BaseRequest.__init__(self, self.ConstApiUrl(),
                                      {"zws-id": zws_id, "address": address,
                                       "citystatezip": citystatezip})

