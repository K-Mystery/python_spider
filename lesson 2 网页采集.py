import requests

# 1.获取URL
# UA:User-Agent 伪装
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36"}
url = "https://www.sogou.com/web"
# 2.处理URL参数，封装到字典中
kw = input("enter a world: ")
param = {
    'query':kw
}
# 3.对指定的URL发起的请求对应的URL是携带参数的，并且在请求过程中处理了参数
response = requests.get(url=url,params=param,headers=headers)
page_text = response.text
fileName = kw+".html"
with open(fileName,'w',encoding='UTF-8') as fp:
    fp.write(page_text)
print(fileName+"爬取成功")

