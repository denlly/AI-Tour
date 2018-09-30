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


class BingbgDownloader:
    _request_url = ''
    _count = 0

    def __init__(self, path):
        self._request_url = path
        ssl._create_default_https_context = ssl._create_unverified_context

    # 开始爬
    def runCatch(self):
        self._get_request_info(self)

        # 获取请求信息beautifulsoup4
    def _get_request_info(self, count):
        fullpath = self._request_url
        stream = urllib.request.urlopen(fullpath)
        data = BeautifulSoup(stream.read())
        print("data", data)

        jsonObject = json.loads(bytes.decode(data))
        # self._get_img_in_response(jsonObject)
        print("data", jsonObject)

    # 解释出图片信息内容
    def _get_img_in_response(self, data):
        # fileArray = []
        # print(data["images"])
        os.mkdir(os.path.join('./', 'img'))
        for img in data["images"]:
            self._download_img(img["url"], './img/%s.jpg' % (img["hsh"]))
        else:
            pass
        #     print(fileobject)

    def downImg(self, count):
        if count < 1:
            count = 1
        self._get_request_info(count)

    def helloPython(self):
        print("hello Python")


if __name__ == "__main__":
    dl = BingbgDownloader(
        "https://docs.scipy.org/doc/numpy/reference/generated/numpy.zeros_like.html#numpy.zeros_like")
    dl.runCatch()
