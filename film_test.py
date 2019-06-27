#从豆瓣爬取西安最近上映的电影
import requests
import re
url="https://movie.douban.com/cinema/nowplaying/xian/"
#响应
response=requests.get(url)
#编码方式
response.encoding="utf-8"
html=response.text
#print(html)
#movies=re.findall(r'<ul class="lists">(.*?)</ul>',html,re.S)[0]
#print(movies)
# 正在上映电影评分
movies_grade = re.findall(r'<span class="subject-rate">(.*?)</span>', html, re.S)
#print(movies_grade)
# movies_all=re.findall(r'<ul class="lists">(.*?)</ul>',html,re.S)
# movies_all=re.findall(r'<li\n                        id="(.*?)"\n                        class="(.*?)"\n                        data-title="(.*?)"\n                        data-score="(.*?)"\n                        data-star="(.*?)"\n                        data-release="(.*?)"\n                        data-duration="(.*?)"\n                        data-region="(.*?)"\n                        data-director="(.*?)"\n                        data-actors="(.*?)"\n                        data-category="(.*?)"\n                        data-enough="(.*?)"\n                        data-showed="(.*?)"\n                        data-votecount="(.*?)"\n                        data-subject="(.*?)"\n                    > ',movies_all,re.S)
movies_all=re.findall(r'<li class="stitle">(.*?)</li>',html,re.S)
movies_all=re.findall(r'<a href="(.*?)"\n                                    class="ticket-btn"\n                                    target="_blank"\n                                    title="千与千寻"\n                                    data-psource="title">\n                                    千与千寻\n                                </a>',movies_all,re.S)
# movies_all=re.findall(r'',movies_all,re.S)
print(movies_all)


# movies_names=re.findall(r'[title="(.*?)"\n]',movies,re.S)
# print(movies_names)



