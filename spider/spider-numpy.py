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
            param = ParamObj(name=param_names[i],type=param_types[i],desc=param_descs[i])
            params.append(param)
        returns = functionHtml.find("dl",class_="last")
        seealso = functionHtml.find("div",class_="seealso")
        examples = functionHtml.find("div",class_="highlight")
        print(title)
        print(html_decode(method))
        print(html_decode(summary))
        return ApiDetail(
            html_decode(title),
            html_decode(method),
            html_decode(summary),
            params,
            returns=[returns],
            seealsos=[seealso],
            examples=[examples])

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



    
        