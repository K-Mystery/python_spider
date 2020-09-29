# 在终端中
# 1.创建一个工程
scrapy startproject xxxPro
# 2. 移动到工程目录内
cd xxxPro
# 3.在spiders子目录中创建一个爬虫文件
scrapy genspider spiderName www.xxx.com
# 4.执行工程
scrapy crawl SpiderName
