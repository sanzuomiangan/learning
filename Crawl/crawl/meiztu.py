
import sys
import os
from config import BaseConfig

class MeiZiTu(BaseConfig):
    def __init__(self):
        super(MeiZiTu,self).__init__()
        self.spider_info = self.recursion.get_value(self.enum,'mzitu')
        self.start_url = self.recursion.get_value(self.spider_info,'start_url')
        self.home_page_xpaths = self.recursion.get_value(self.spider_info,'home_page_xpaths')
        self.base_url = self.recursion.get_value(self.spider_info,'base_url')
        self.number = 0
        self.num = 0
    def get_tags_page_num(self,all_page_info):
        """pass"""

        page_urls,page_numbers,page_names = all_page_info[0],all_page_info[1],all_page_info[2]
        for page_url,page_num,page_name in zip(page_urls,page_numbers,page_names):
            img_name =(str(self.number) + page_name)
            self.create_folder(img_name)

            self.number +=1
            all_page_num = int(int(page_num.split(' ')[-1].split('[')[1].split(']')[0]) / 4)
            for _page_num in range(1,all_page_num + 1):
                if _page_num == 1:
                    new_url = page_url
                else:
                    new_url = page_url[:-5] + '_{}.html'.format(_page_num) 
                #print(self.number,new_url,page_name,num)
                self.download_img(new_url, img_name)
    def get_home_page(self):
        all_page = self.get_all_page()
        all_page.append(self.start_url)
        #print(all_page)
        for item in all_page:
            param = self.output(self.start_url,self.home_page_xpaths)
            self.get_tags_page_num(param)
    def get_all_page(self):
        """pass"""
        all_page_num = self.recursion.get_value(self.spider_info,'all_page_num')
        return [self.base_url.format(page_num)for page_num in range(2,all_page_num + 1)]
    def create_folder(self,img_name):
        if not os.path.exists(os.path.abspath('img/'+img_name)):   # 是判断 os.path.abspath('图片名称') 这个文件夹是
            os.mkdir(os.path.abspath('img/'+img_name))   # 如果不存在 通过os.mkdir 在这个路径下创建一个img_name的文件夹
        self.num = 0
    def download_img(self,new_url,name):
        for i in range(1,5):
            #_img = self.output(new_url,'//img/@src')[i]
            #print(new_url)
            _img = self.output(new_url,'//img/@src')[i]
            print(_img)
            print('=====')
            download_path =os.path.abspath('img/'+name) + '/{}.jpg'.format(name + str(self.num))
            print(download_path)
            self.num += 1
            with open(download_path, 'wb') as file:
                file.write(self.output(_img))
    def main(self):
        self.get_home_page()

