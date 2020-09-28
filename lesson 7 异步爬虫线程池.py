import requests
from lxml import etree
import re
from multiprocessing.dummy import Pool
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36"}
# 原则：线程池处理的是阻塞且耗时的操作
url = 'https://www.pearvideo.com/category_5'
page_text = requests.get(url=url,headers=headers).text
tree = etree.HTML(page_text)
li_list = tree.xpath('//*[@id="listvideoListUl"]/li')
urls = [] #存储视频链接和名字
for li in li_list:
    detail_url = 'https://www.pearvideo.com/'+li.xpath('./div/a/@href')[0]
    name = li.xpath('./div/a/div[2]/text()')[0] + '.mp4'
    print(detail_url,name)
    detail_page_text = requests.get(url=detail_url,headers=headers).text
    # 对于异步加载需要使用正则表达式
    # 从此处开始会报错，仅仅记录线程池的用法
    ex = 'srcUrl="(.*?)",vdoUrl'
    video_url = re.findall(ex,detail_page_text)[0]
    dic = {
        'name':name,
        'url':video_url
    }
    urls.append(dic)
def get_video_data(dic):
    url = dic['url']
    print(dic['name'],'正在下载...')
    data = requests.get(url=url,headers = headers).content
    # 持久化存储
    with open(dic['name'],'wb',) as fp:
        fp.write(data)
        print(dic['name'],'下载成功')
# 使用线程池，较为耗时
pool = Pool(4)
pool.map(get_video_data,urls)

pool.close()
pool.join()
