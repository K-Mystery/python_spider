import requests
from lxml import etree

url = 'https://euw.op.gg/champion/statistics'
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36",
           "Accept-Language": "zh-CN,zh;q=0.9"}
page_text= requests.get(url=url,headers = headers).text
page_text.encode('utf-8')
# print(page_text)
tree = etree.HTML(page_text)
list = tree.xpath("//div[@class='champion-index__champion-list']/div")
fp = open("英雄联盟.txt",'w',encoding='utf-8')
for li in list:
    champion_name = li.xpath('.//div[@class="champion-index__champion-item__name"]/text()')[0]
    fp.write(champion_name+'\n')
    print(champion_name,"爬取成功")
fp.close()
