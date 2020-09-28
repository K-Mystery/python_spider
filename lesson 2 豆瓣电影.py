import requests
import json

url = 'https://movie.douban.com/j/chart/top_list'
param = {
    'type': '13',
'interval_id': '100:90',
'action':'',
'start': '0',
'limit': '20',
}
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36"}
response = requests.get(url=url,params=param,headers=headers)
list_data = response.json()
fileName = "豆瓣"+'.json'
with open(fileName,'w',encoding='utf-8') as fp:
    json.dump(obj=list_data,fp=fp,ensure_ascii=False)
print("豆瓣爬取结束！")
