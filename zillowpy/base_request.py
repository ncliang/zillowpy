#/usr/bin/python
"""
Created on Apr 19, 2011

@author: ncliang
"""

import urllib
import urllib2

from zillowpy import zillow_response


class BaseRequest(object):
  """classdocs"""

  REQ_SUCCESS = 0
  SERVICE_ERROR = 1
  INVALID_ZWSID = 2
  SERVICE_UNAVAILABLE = 3
  API_UNAVAILABLE = 4

  API_URL_TEMPLATE = "http://www.zillow.com/webservice/%s.htm"

  def __init__(self, api_url, parameters):
    """Constructor"""
    self._api_url = api_url
    self._parameters = parameters

  def ConstApiUrl(self):
    return self.API_URL_TEMPLATE % self.__class__.__name__

  def Execute(self):
    resp_str = urllib2.urlopen(
        self._api_url, urllib.urlencode(self._parameters)).read()
    return zillow_response.ZillowResponse(resp_str)