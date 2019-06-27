#下载一个小说:奇书网：老人与海，只有1-14章节
# https://wap.qisuu.la/du/2/2976/index_2.html
# -*- coding:utf-8 -*-
import requests
import re
url="https://wap.qisuu.la/Shtml2976.html"
#响应
response=requests.get(url)
#编码方式
response.encoding="utf-8"
html=response.text
#print(html)
title=re.findall(r'<h3>(.*?)</h3>',html,re.S)[0]
#print(title)
#获取每一章的信息：章节，url
ul=re.findall(r'<div class="list_xm">.*?</div>',html,re.S)[1]#[1]代表第二次出现
#re.S代表匹配不可见字符
print(ul)
chapter_info_list=re.findall(r'<a href="(.*?)">(.*?)</a>',ul,re.S)
#exit()
#print(chapter_info_list)
#新建一个文件，保存下载的文件
fb=open('%s.txt'% title,'w',encoding='utf-8')
#循环每一章节，分别去下载
for chapter_info in chapter_info_list[:14]:#特殊处理，因为最好一个不是章节，是下一页
    chapter_url,chapter_title=chapter_info
    chapter_url="https://wap.qisuu.la%s"%chapter_url
    #print(chapter_url,chapter_title)
    #下载章节内容
    chapter_rsponse=requests.get(chapter_url)
    chapter_rsponse.encoding='utf-8'
    chapter_html=chapter_rsponse.text
    #print(chapter_html)

    chapter_content=re.findall(r'<div id="novelcontent" class="novelcontent">.*?</div>',chapter_html,re.S)[0]
    chapter_content=re.findall(r'<p>(.*?)</p>',chapter_content,re.S)[0]
    #数据清洗
    #空格变为空
    chapter_content=chapter_content.replace(' ','')
    #&nbsp;变为空
    chapter_content=chapter_content.replace('&nbsp;','')
    chapter_content=chapter_content.replace('<br/>','')
    #持久化
    fb.write(chapter_title)
    fb.write('\n')
    fb.write(chapter_content)
    fb.write('\n')
    print(chapter_url)