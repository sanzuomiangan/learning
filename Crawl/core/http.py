

from requests import Session
from lxml import etree

class HttpHandler:
    seesion = Session()
    
    @classmethod
    def request(cls,url,encoding='utf-8'):
        """pass"""
        resp = cls.seesion.get(url)
        if encoding:
            resp.encoding = encoding
        return resp
    
    @classmethod
    def parse(cls,html,xpath):
        """pass"""
        return etree.HTML(html).xpath(xpath)
    @classmethod
    def output(cls,url,xpaths=None):
        """pass"""
        html = cls.request(url).content
        if isinstance(xpaths,list):
            return [cls.parse(html, xpath) for xpath in xpaths]
        if not xpaths:
            return html
        return cls.parse(html, xpaths)