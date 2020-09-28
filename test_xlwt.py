import xlwt

workbook = xlwt.Workbook(encoding="utf-8")  #创建workbook对象
worksheet = workbook.add_sheet('sheet1')    #创建工作表
# # worksheet.write(0,0,'hello')    #写入数据，第一行参数“行”，第二个参数“列”，第三个参数内容
titles = [1,2,3,4,5,6,7,8,9,10,11]
for i in range(0,len(titles)):
    worksheet.write(0,i,titles[i])
score_list = []
for i in range(2,5):
    a =1
    b =2
    c =3
    d = 4
    e = 5
    f = 6
    g =7
    h = 8
    m = 9
    score_list.append((i,a,b,c,d,e,f,g,h,m))
    for j in range(0,len(titles)-1):
        worksheet.write(i-1,j+1,(score_list[i-2])[j])

print(score_list)
workbook.save('student.xls')

