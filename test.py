# -*- coding: utf-8 -*-
import requests
import re

baseUrl = "http://tdzx.fuzhou.gov.cn/zz/tdjy/zpgjg/"

url_response = requests.get(baseUrl)
if url_response.status_code != 200:
    print(url_response.status_code)
    pass

respons_text = url_response.text

pattern = re.compile("<a href=\"(.+\.htm)\".+>宗地.+<\/a>")
CurPageRets = pattern.findall(respons_text)

p2 = re.compile("<td class=\"co1\"><p>地块位置：<\/p><\/td>\s+<.+\"co2\">(\W+)<\/td>")
for item in CurPageRets:
    iUrl = baseUrl + item
    iR = requests.get(iUrl)
    print p2.findall(iR.text)
    pass


















