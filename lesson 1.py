import requests

# 1.制定Url
url = "https://www.sogou.com/"
# 2.发起请求
response = requests.get(url=url)
response.encoding = 'utf-8'
# 3.获取相应数据
page_text = response.text
# 4.持久化存储
with open("./sogou.html",'w',encoding="UTF-8") as fp:
    fp.write(page_text)
print("爬取结束")
