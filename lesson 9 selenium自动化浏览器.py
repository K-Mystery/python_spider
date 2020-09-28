from selenium import webdriver
from selenium.webdriver import ActionChains
from lxml import etree
from time import sleep

# 初始化浏览器对象
bro = webdriver.Chrome(executable_path='./chromedriver.exe')

# # 药监局实例
#
# # 让浏览器发起一个制定的URL请求
# bro.get('http://scxk.nmpa.gov.cn:81/xk/')
#
# # 获取浏览器当前页面的源码数据
# page_text = bro.page_source
#
# # 解析企业名称
# tree = etree.HTML(page_text)
# li_list = tree.xpath('//*[@id="gzlist"]/li')
# for li in li_list:
#     name = li.xpath('./dl/@title')[0]
#     print(name)
#
# sleep(5)
# bro.quit()

# # 淘宝实例

# bro.get('https://world.taobao.com/')
# search_input = bro.find_element_by_id('mq')
#
# # 标签交互
# search_input.send_keys('Iphone') #搜索框
# #执行一组javascript程序
# bro.execute_script('window.scrollTo(0,document.body.scrollHeight)')
#
# btn = bro.find_element_by_xpath('//*[@id="J_PopSearch"]/div[1]/div/form/input[2]')
# btn.click()
#
# bro.get("https://www.baidu.com/")
# sleep(2)
# bro.back()  # 后退
# sleep(2)
# bro.forward() # 前进
#
# sleep(5)
# bro.quit()


# iframe 实例
# 如果需要操作的网页涉及到iframe，不能直接定位，需要如下操作
bro.get('https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable')
bro.switch_to.frame('iframeResult')
div = bro.find_element_by_xpath('//*[@id="draggable"]')

# 动作链
action = ActionChains(bro)
action.click_and_hold(div) # 点击长按制定的标签

for i in range(5):
    #perform()立即执行动作链操作
    action.move_by_offset(17,0).perform()
    sleep(0.3)

action.release() #释放动作链

sleep(5)
bro.quit()

# 额外的记录

# 网页截图
bro.save_screenshot('example.png')
# 定位验证码图片
code_img = bro.find_elements_by_xpath('')
# 图片起始坐标，返回一个字典
location = code_img.location
# 图片长和宽，返回一个字典
size = code_img.size
# 左上角和右下角坐标
range = (int(location['x']),int(location['y'],int(location['x']+size['width'],int(location['y']+size['height']))))
