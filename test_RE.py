import re
#   正则表达式
pat = re.compile("AA")  #正则表达式，验证其他字符串,AA为需要匹配的内容
#   创建模式对象

# m = pat.search("ABCAA")    # 被校验的内容

# 没有模式对象
# m = re.search("AA","ABCAA") # 前面是规则（模板），后面是被校验的对象

# 查找所有符合的字符串，并返回一个列表
# m = re.findall("a","abcdabcdabcd")
# n = re.findall("[A-Z]","AaBbCcDdEeFfGg")

#sub替换
m = re.sub("a","A","abcdefgh") #第一个被替换的内容，第二个是替换成的内容，第三个是需要执行替换工作的字符串

print(m)
