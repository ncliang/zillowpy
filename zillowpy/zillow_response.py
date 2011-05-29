#/usr/bin/python
"""
Created on Apr 19, 2011

@author: ncliang
"""

from xml.etree import ElementTree
import urllib


class ZillowResponse(object):
  
  def __init__(self, raw_resp_str):
    self._dom = ElementTree.XML(raw_resp_str)

  def __getattr__(self, name):
    self._ParseDom(self._dom, self.__dict__)
    if name not in self.__dict__:
      raise AttributeError
    return self.__dict__[name]

  # object() does not contain __dict__, must subclass...
  class _DictClass(object):
    pass

  def _ParseDom(self, node, parent_dict):
    if node.text and node.text.strip():
      parent_dict[self._NodeNameToDictKey(node.tag.strip())] = node.text.strip()
      return

    child_dict = self._DictClass()
    for child in node.getchildren():
      self._ParseDom(child, child_dict.__dict__)
    parent_dict[self._NodeNameToDictKey(node.tag.strip())] = child_dict

  def _NodeNameToDictKey(self, name):
    name_start = name.find("}")
    if name_start != -1:
      name = name[name_start+1:]
    return urllib.quote(name)

