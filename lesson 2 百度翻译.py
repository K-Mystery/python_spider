import requests
import json
# post 请求
# 响应数据是json数据
post_url = "https://fanyi.baidu.com/sug"
# post请求和get处理一致
data = {"kw":"dog"}
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36"}

resposne = requests.post(url=post_url,data=data,headers = headers)
# 获取相应数据 json()方法返回的是一个对象（如果确认响应数据是json类型），根据content-type判断
dict_obj = resposne.json()
print(dict_obj)

with open('./dog.json','w',encoding='utf-8') as fp:
    json.dump(dict_obj,fp=fp,ensure_ascii=False)
print("over")
