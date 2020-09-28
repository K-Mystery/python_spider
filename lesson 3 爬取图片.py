import requests
import re
import os
import lxml


# 单个图片案例
# url = 'https://pic.qiushibaike.com/system/pictures/12360/123606350/medium/2X2XLIK3Y1EYI1KC.jpg'
# headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36"}
# response = requests.get(url = url)
# # content 返回的是二进制格式的数据
# img_data = response.content
# with open('./qiutu.jpg','wb') as fp:
#     fp.write(img_data)
# print('爬取成功')

# 爬取整个页面
if not os.path.exists("./qiutulibs"):
    os.mkdir('./qiutulibs')
url = 'https://www.qiushibaike.com/imgrank/'
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36"}
page_text = requests.get(url=url,headers=headers).text
id_list = re.findall('<div class="thumb">.*?<a href="(.*?)" target.*?</div>',page_text,re.S)
img_list = []
id = id_list[0]
id_url = 'https://pic.qiushibaike.com'+id
response = requests.get(id_url,headers = headers).text
# em = '<div class="thumb">.*?<img src = "(.*?)" alt.*?</div>'
# img_list = re.findall(response,em,re.S)
print(response)
# for src in img_list:
#     img_url = 'https:'+src
#     img_data = requests.get(img_url,headers).content
#     img_name = src.split('/')[-1]
#     img_path = './qiutulibs/'+img_name
#     with open(img_name,'wb') as fp:
#         fp.write(img_data)
#     print('抓取成功')
