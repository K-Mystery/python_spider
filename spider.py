import sys
from bs4 import BeautifulSoup
import re
import urllib
import urllib.request
import urllib.error
import xlwt


def main():
    baseurl = "https://movie.douban.com/top250?start="
    # 1.爬取网页
    datalist = getData(baseurl)
    savepath = '.\\豆瓣电影Top250.xls'
    #3.保存数据
    saveData(datalist,savepath)

# 影片详情的链接
findLink = re.compile(r'<a href="(.*?)">') #创建正则表达式对象，表示规则（字符串的模式）
# 影片图片的链接
findImgSrc = re.compile(r'<img.*src="(.*?)"',re.S)  #re.S忽略换行符
#   影片片名
findTitle = re.compile(r'<span class="title">(.*)</span>')
#   影片评分
findRating = re.compile(r'<span class="rating_num" property="v:average">(.*)</span>')
# 找到评价人数
findJudge = re.compile('<span>(\d*)人评价</span>')
#   找到介绍
findInq = re.compile(r'<span class="inq">(.*)</span>')
#   找到影片的相关内容
findBd = re.compile(r'<p class="">(.*?)</p>',re.S)



# 爬取网页
def getData(baseurl):
    datalist = []
    for i in range(0,10): #调用获取页面信息的函数，10次，左闭右开
        url = baseurl + str(i*25)
        html = askURL(url)
        # 逐一解析数据
        soup = BeautifulSoup(html,"html.parser")
        for item in soup.find_all('div',class_="item"):    #查找符合要求的字符串，形成列表,class_表示属性值
            # print(item) #测试，查看item全部信息
            data = [] #保存一部电影的所有信息
            item = str(item)

            #   影片详情链接
            link = re.findall(findLink,item)[0] #re库用来通过正则表达式查找特定的字符串
            data.append(link)   #添加链接

            imgSrc = re.findall(findImgSrc,item)[0]
            data.append(imgSrc) #添加图片

            titles = re.findall(findTitle,item) #片名可能只有一个中文名，没有外国名
            if(len(titles) == 2):
                ctitle = titles[0]  #添加中文名
                data.append(ctitle)
                otitle = titles[1].replace("/","")  #去掉无关的符号
                data.append(otitle)
            else:
                data.append(titles[0])
                data.append(' ')    #外国名字留空

            rating = re.findall(findRating,item)[0]
            data.append(rating)

            judgeNum = re.findall(findJudge,item)[0]
            data.append(judgeNum)

            inq = re.findall(findInq,item)
            if len(inq) != 0:
                inq = inq[0].replace("。","")
                data.append(inq)
            else:
                data.append(" ")

            bd = re.findall(findBd,item)[0]
            bd = re.sub('<br(\s+)?/>(\s+)?'," ",bd) #去掉（br/)
            bd= re.sub('/'," ",bd)  #替换/
            data.append(bd.strip()) #去掉前后的空格

            datalist.append(data)   #处理好的一部电影信息放入datalist


    return datalist


# 得到制定一个URL的网页内容
def askURL(url):
    head = {    #模拟浏览器头部信息
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36"
    }
    # 用户代理，表示告诉服务器，我们可以接受什么文件

    request = urllib.request.Request(url, headers = head)
    html = ""
    try:
        response = urllib.request.urlopen(request)
        html = response.read().decode("UTF-8")

    except urllib.error.URLError as e:
        if hasattr(e,"code"):
            print(e.code)
        if hasattr(e,"reason"):
            print(e.reason)

    return html

# 保存数据
def saveData(datalist,savepath):
    book = xlwt.Workbook(encoding="utf-8",style_compression=0)  #创建workbook对象
    sheet = book.add_sheet('豆瓣电影',cell_overwrite_ok=True)
    col = ("电影详情链接","电影图片","影片中片名","影片外文名","影片评分","评价人数","影片介绍","影片相关内容")
    for i in range(0,len(col)):
        sheet.write(0,i,col[i]) #列名
    for i in range (0,250):
        print("第%d条"%(i+1))
        data = datalist[i]
        for j in range (0,len(col)):
            sheet.write(i+1,j,data[j])

    book.save('Student.xls')






if __name__ == "__main__":
#调用函数
    main()
    print("爬取完毕")
