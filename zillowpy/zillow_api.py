#/usr/bin/python
"""
Created on May 20, 2011

@author: ncliang
"""

from zillowpy import base_request
from zillowpy import zillow_interface
import new


PARAM_MAP = {
    "zws_id": "zws-id",
    "unit_type": "unit-type",
    "chart_duration": "chartDuration",
    "posting_type": "postingType"
    
}


def ConstructCtorStr(api_name, req_params, opt_params=[]):
  opt_params_with_none = ["%s=None" % param for param in opt_params]
  params = req_params + opt_params_with_none
  ctor_list = ["def _%sCtor(self, " % api_name]
  ctor_list.append(", ".join(params))
  ctor_list.append("):\n")

  ctor_list.append("  params = {")
  ctor_list.append(", ".join(
      ["\"%s\": %s" % (PARAM_MAP.get(param, param), param) for param in req_params]))
  ctor_list.append("}\n")

  for param in opt_params:
    ctor_list.append("  if %s:\n" % param)
    ctor_list.append("    params[\"%s\"] = %s\n" % (PARAM_MAP.get(param, param),
                                                    param))

  ctor_list.append("  base_request.BaseRequest.__init__(self, self.ConstApiUrl(), params)")
  return "".join(ctor_list)


for zint in zillow_interface.ZILLOW_API_INTERFACE:
  exec(ConstructCtorStr(zint.api_name, zint.req_params, zint.opt_params))
  locals()[zint.api_name] = new.classobj(
      zint.api_name,
      (base_request.BaseRequest,),
      {"__init__": locals()["_%sCtor" % zint.api_name]})

