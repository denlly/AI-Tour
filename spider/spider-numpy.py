# coding=utf-8

import urllib
import urllib.request
import html.parser
from bs4 import BeautifulSoup
import re
import time
import ssl
import json
import os.path
import os
from tornado.template import Template
import html.parser

def html_decode(s):
    htmlCodes = (
            ("`", '&#39;'),
            ('“', '&quot;'),
            ('>', '&gt;'),
            ('<', '&lt;'),
            ('&', '&amp;')
        )
    for code in htmlCodes:
        s = s.replace(code[1], code[0])
    return s

# 定义ParamObj类
class ParamObj:
    def __init__(self, name='[noName]',type='',desc='',notice=''):
        self.name = name
        self.type = type
        self.desc = desc
        self.notice = notice        

# 定义 Detail 的类
class ApiDetail:
    def __init__(self,title,method,summary,params=[],returns=[],seealsos=[],examples=[]):
        self.title = title
        self.method = method
        self.summary = summary
        self.params = params
        self.returns = returns
        self.seealsos = seealsos
        self.examples = examples

# seealso 类
class Seealso:
    def __init__(self, title, desc,url):
        self.title = title
        self.desc = desc
        self.url = url
        

class BingbgDownloader:
    _request_url = ''
    _count = 0

    def __init__(self, path):
        self._request_url = path
        ssl._create_default_https_context = ssl._create_unverified_context

    # 开始爬
    def runCatch(self):
        # 获取html原始页面
        html = self._get_request_info(self)
        # 提取数据
        dataObj = self._get_detail_info(html)
        # 写入到文件
        self._write_by_template(dataObj)
        return 123

        # 获取请求信息beautifulsoup4
    def _get_request_info(self, count):
        fullpath = self._request_url
        stream = urllib.request.urlopen(fullpath)
        return BeautifulSoup(stream.read(),"html5lib")
        
    def _get_detail_info(self,htmlData):
        html_parser = html.parser.HTMLParser()
        # 解析数据
        title = htmlData.title.text.split(' ')[0]
        functionHtml = htmlData.find("dl", class_="function")
        method = functionHtml.find("dt",id=title).get_text().replace('[source]¶','')
        summary = functionHtml.select("dd > p")[0].get_text()
        paramHtml = functionHtml.find("dl",class_="docutils")
        param_names= paramHtml.find_all("strong")
        param_types = paramHtml.find_all("span", class_="classifier")
        param_descs = paramHtml.find_all("dd")
        params = []
        for i in range(len(param_names)):
            param = ParamObj(name=param_names[i].get_text(),type=param_types[i].get_text(),desc=param_descs[i].get_text().replace("\n", ""))
            params.append(param)
        returnHtml = functionHtml.find("dl",class_="last")
        return_dicts = returnHtml.find_all('strong')
        return_types = returnHtml.find_all('span', class_="classifier")
        return_descs = returnHtml.find_all('p')
        returns = []
        for y in range(len(return_dicts)):
            returnParam = ParamObj(
                name=return_dicts[y].get_text(),
                type = return_types[y].get_text(),
                desc = return_descs[y].get_text()
            )
            returns.append(returnParam);
            
        seealsoHtml = functionHtml.find("div",class_="seealso")
        seealso_titles = seealsoHtml.find_all('a',class_="reference")
        seealso_descs = seealsoHtml.find_all('dd')
        seealsos = []
        for z in range(len(seealso_titles)):
            seealso = Seealso(
                title=seealso_titles[z].get_text(),
                desc=seealso_descs[z].get_text(),
                url = seealso_titles[z]["href"]
            )
            seealsos.append(seealso)

        examples = functionHtml.find("div",class_="highlight")
        return ApiDetail(
            html_decode(title),
            html_decode(method),
            html_decode(summary),
            params,
            returns,
            seealsos,
            examples)

    # 解释出图片信息内容
    def _write_by_template(self, data):
        directory = 'docs/python/numpy'
        templateRst = '_template.rst'
        if os.path.exists(os.path.join(os.getcwd(),directory)) == False:
            os.mkdir(directory)
        outString = ''
        with open(os.path.join(os.getcwd(),directory,templateRst), 'r') as file:
            temp = Template(file.read())
            outString =temp.generate(data=data)
        
        with open(os.path.join(os.getcwd(),directory,data.title+".rst"), 'w', encoding='utf-8') as wf:
            wf.write(outString.decode("utf-8"))

if __name__ == "__main__":
    dl = BingbgDownloader("https://docs.scipy.org/doc/numpy/reference/generated/numpy.zeros_like.html#numpy.zeros_like")
    dl.runCatch()



    
        