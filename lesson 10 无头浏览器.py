from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep

# 无头浏览器参数
chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('disable-gpu')
# 实现规避检测
chrome_options.add_experimental_option('excludeSwitches',['enable-automation'])


bro = webdriver.Chrome(executable_path='./chromedriver.exe',options=chrome_options)
bro.get("https://www.baidu.com")
print(bro.page_source)
sleep(2)
bro.quit()
