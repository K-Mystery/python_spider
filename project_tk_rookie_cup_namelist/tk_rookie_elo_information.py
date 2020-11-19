import re
import requests
from lxml import etree

list = open("tk_rookie_cup.txt", 'r', encoding='utf-8')
lines = list.readlines()
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36",
           "Accept-Language": "zh-CN,zh;q=0.9"}
list.close()
fp = open("tk_rookie_cup_elo.txt", 'w', encoding='utf-8')
for line in lines:
    str1 = "Summoner Name:"

    if str1 in line:
        str = re.compile("Summoner Name: ")
        player_name_temp = re.split(str,line)
        player_name = player_name_temp[1]
        player_url = "https://euw.op.gg/summoner/userName="+player_name
        page_text = requests.get(url=player_url,headers=headers).text
        tree = etree.HTML(page_text)
        tier_solo = tree.xpath("//*[@id='SummonerLayoutContent']/div[2]/div[1]/div[1]/div/div[2]/div[2]/text()")
        tier_group = tree.xpath("//*[@id='SummonerLayoutContent']/div[2]/div[1]/div[2]/div/div[2]/text()")
        fp.write('\n'+player_name+'\n')
        fp.write("单双排段位："+tier_solo[0].strip()+'\n')
        fp.write("组排段位："+tier_group[0].strip()+'\n')
        print("队员爬取成功")
    else:
        team_name = line
        fp.write('\n')
        fp.write('*'*20)
        fp.write('\n'+team_name+'\n')
        print("队名输入成功")
fp.close()
print("爬取完毕")



