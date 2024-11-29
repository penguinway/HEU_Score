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

#todo:
#1.添加一个功能，填写过一次账号密码，就保存到配置文件中，就不用再输入了
#2.当前输入密码时，密码没有隐藏，需要改善
#3.添加几种输出文件格式，输出样式自拟
#4.改善异常处理，当前基本完全没有异常处理

