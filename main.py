from score import cal_by_first, cal_by_second
from web import JWGLWeb

username = input("请输入你的学号:")
password = input("请输入你的密码:")
web = JWGLWeb(username, password)
web.login()
choose = input("选择使用哪种方法计算成绩:1.使用账号密码从学校网站获取 2.使用学校网站导出的Excel文件获取\n")
if choose == "1":
    web.getjson()
    cal_by_first()
if choose == "2":
    cal_by_second()
