#/usr/bin/python
"""
Created on May 20, 2011

@author: ncliang
"""

from zillowpy import base_request


class GetZestimate(base_request.BaseRequest):
  """classdocs"""

  INVALID_ZPID = 500
  ZPID_NOT_FOUND = 501
  NO_ZESTIMATE = 502

  def __init__(self, zws_id, zpid):
    """Const."""
    base_request.BaseRequest.__init__(self, self.ConstApiUrl(),
                                      {"zws-id": zws_id, "zpid": zpid})