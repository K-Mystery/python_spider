from selenium import webdriver
from time import sleep
from PIL import Image
from selenium.webdriver.chrome.options import Options

# chrome_options = Options()
# chrome_options.add_argument('--headless')
# chrome_options.add_argument('disable-gpu')
# # 实现规避检测
# chrome_options.add_experimental_option('excludeSwitches',['enable-automation'])

# bro = webdriver.Chrome(executable_path='./chromedriver.exe',options=chrome_options)
bro = webdriver.Chrome(executable_path='./chromedriver.exe')
bro.maximize_window()

bro.get('https://www.12306.cn/index/')
search_input = bro.find_element_by_xpath('//*[@id="J-header-login"]/a[1]')
search_input.click()

sleep(5)

anmelden = bro.find_element_by_xpath('/html/body/div[2]/div[2]/ul/li[2]/a')
anmelden.click()

sleep(5)

bro.save_screenshot('test.png')

code_img = bro.find_element_by_xpath('//*[@id="J-loginImg"]')
# 图片起始坐标，返回一个字典
location = code_img.location
# 图片长和宽，返回一个字典
size = code_img.size
# 左上角和右下角坐标
range = (int(location['x']),int(location['y']),int(location['x']+size['width']),int(location['y']+size['height']))
i = Image.open('./test.png')
code_img_name = './code.png'
frame = i.crop(range)
frame.save(code_img_name)

sleep(5)
bro.quit()
