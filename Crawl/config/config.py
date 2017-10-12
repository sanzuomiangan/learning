

"""pass"""

from core.http import HttpHandler
from core.recursion import GetDictParam

class BaseConfig(GetDictParam,HttpHandler):
    """pass"""
    enum = {
        "mzitu":{
            "all_page_num":25,
            "start_url":"https://www.meitulu.com/t/nvshen/",
            "base_url":"https://www.meitulu.com/t/nvshen/{}.html", 
            "xpaths":{
                "home_page_xpaths":[
                    '//ul[@class ="img"]/li/a/@href', 
                    '//ul[@class ="img"]/li/a/img/@alt',
                    '//ul[@class ="img"]/li/p[3]/a/text()'
                ],
                "download_img_xpaths":[
                    '//div[@class ="content"]/center/img/@src',
                    '//div[@class ="content"]/center/img/@alt' 
                ],
                "down_img_url":[
                    "//img/@src" 
                ]
                
                }
            
            
            
            }
        
        
        
        }
    def __init__(self):
        """pass"""
        self.recursion = GetDictParam()
        self.get_value = self.recursion.get_value
        self.list_for_key_to_dict = self.recursion.list_for_key_to_dict