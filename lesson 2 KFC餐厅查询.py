import requests
import json

url = 'http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=keyword'
kw = input("请输入一个城市： ")
data = {
    'cname':'' ,
'pid': '',
'keyword': kw,
'pageIndex': '1',
'pageSize': '10',
}
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36"}
response = requests.post(url = url,data=data,headers=headers)
list_data = response.json()
with open('./KFC.json','w',encoding='utf-8') as fp:
    json.dump(list_data,fp=fp,ensure_ascii=False)
print("肯德基爬取成功")
