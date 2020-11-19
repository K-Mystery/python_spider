import requests
from lxml import etree

url = 'https://www.toornament.com/en_GB/tournaments/4022168603762335744/participants/'
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36",
           "Accept-Language": "zh-CN,zh;q=0.9"}
page_text= requests.get(url=url,headers = headers).text
page_text.encode('utf-8')
# print(page_text)
tree = etree.HTML(page_text)
list = tree.xpath("//*[@id='main-container']/div[3]/section/div/div[2]/div")
fp = open("tk_rookie_cup.txt", 'w', encoding='utf-8')
for li in list:
    url_team = li.xpath('.//a/@href')
for team in url_team:
    new_url = "https://www.toornament.com"+team+"info"
    page_text_team = requests.get(url = new_url,headers = headers).text
    page_text_team.encode('utf-8')
    tree2 = etree.HTML(page_text_team)
    player_name = tree2.findall(".//div[@class='text secondary small summoner_player_id']")
    temp_list = tree2.xpath("//*[@id='main-container']/div[3]/section/div/div[2]/div/div")
    for temp in temp_list:
        team_name = temp.xpath("./div/div[1]/div/div[1]/h3/text()")
        fp.write(team_name[0]+'\n')
        print("队名爬取完毕")
        player_name_list = temp.findall(".//div[@class='text secondary small summoner_player_id']")
        for player_name_temp in player_name_list:
            player_name = player_name_temp.xpath("normalize-space(./text())")


            fp.write(player_name+'\n')
        print("队员爬取完毕")
        # player_name = temp.findall("normalize-space(.//div[@class='text secondary small summoner_player_id']/text())")
fp.close()

# fp = open("tk_rookie.txt",'w',encoding='utf-8')
# for li in list:
#     champion_name = li.xpath('.//div[@class="champion-index__champion-item__name"]/text()')[0]
#     fp.write(champion_name+'\n')
#     print(champion_name,"爬取成功")
# fp.close()
