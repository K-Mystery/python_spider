from bs4 import BeautifulSoup

file = open("./Baidu.html", "rb")
html = file.read()
bs = BeautifulSoup(html,"html.parser")


# print(bs.title)
# print(bs.title.string)
# print(bs.head)
# # 1. Tag 标签及其内容，拿到第一个内容
#
# print(bs.a.attrs) # 获取超链接中的所有属性，返回一个字典值

# ——————————————————————————————
# 文档的遍历
print(bs.head.contents) # 获取head的所有子节点，以列表形式返回，可以加后缀[]选择特定内容

# # 文档的搜索
# # 1.find_all()
# # 字符串过滤，查找和字符串完全匹配的内容
# t_list = bs.find_all("a")

# # 正则表达式搜索：使用search()方法来匹配内容
# import re
# t_list = bs.find_all(re.compile("a")) #只要标签含a，都会导入进来

# # 方法： 传入一个函数（方法），根据函数的要求来搜索
# def name_is_exists(tag):
#     return tag.has_attr("name")
#
# t_list = bs.find_all(name_is_exists())


# print(t_list)

# 2.kwargs 参数
t_list = bs.find_all(id="head")

# 3. test 参数
t_list = bs.find(text="hao123")

# 4. limit参数
t_list = bs.find_all("a",limit=3) # 限定数量

# css选择器
t1 = bs.select('titile') #通过标签查找
t2 = bs.select('.mnav') # 通过类查找
t3 = bs.select('#v1') #  通过id查找
t4 = bs.select("a[class='bri']") #通过属性来查找
t5 = bs.select('head > title') #通过子标签来查找
t6 = bs.select('.mnav ~ .bri') #通过兄弟标签来查找，.mnav层次的名为bri的兄弟标签
