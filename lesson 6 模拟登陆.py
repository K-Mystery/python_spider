import requests
# 遇到验证码需要先获得验证码图片进行保存，再对验证码进行识别，然后再输入结果

# 登录的时候是一个post请求，在data填入用户名等相关信息

# 保持登录需要用到cookie，获得cookie可以用requests里的Session

session = requests.Session
response = session.post()
response_get = session.get()

# 代理ip
requests.get(url=url,proxies={'https':'192.168.1.1'}) #对应不同的协议
requests.get(url=url,proxies={'http':'192.168.1.1'})
