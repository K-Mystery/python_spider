from bs4 import BeautifulSoup
import requests
import lxml
import re

url = 'https://www.shicimingju.com/book/sanguoyanyi.html'
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36"}
page_text = requests.get(url=url,headers=headers).text
soup = BeautifulSoup(page_text,'lxml')
list = soup.select(".book-mulu> ul > li")
with open("./三国.txt",'w',encoding='utf-8') as fp:
    for li in list:
        title = li.a.string
        detail_url ='https://www.shicimingju.com' + li.a['href']
        detail_page = requests.get(url=detail_url,headers = headers).text
        detail_soup = BeautifulSoup(detail_page,'lxml')
        div_tag = detail_soup.find("div",class_ = "chapter_content")
        content = div_tag.text
        fp.write(title + ':' + content + '\n')
        print(title,'爬取成功！')

# 通用解决中文乱码
# 假设一张图片
imgname = ''+'.jpg'
imgname = imgname.encode('iso-8859-1').decode('gbk')

