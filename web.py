from DrissionPage import ChromiumPage, SessionPage
from DrissionPage.common import By
import ddddocr
from urllib import parse
import base64
import time
import requests
import json


class JWGLWeb:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.page = ChromiumPage()
        self.headers = {
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Connection': 'keep-alive',
            'Host': 'jwgl.hrbeu.edu.cn',
            'Origin': 'https://jwgl.hrbeu.edu.cn',
            'Referer': 'https://jwgl.hrbeu.edu.cn/jwapp/sys/cjcx/*default/index.do?THEME=green&EMAP_LANG=zh',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
            'X-Requested-With': 'XMLHttpRequest',
            'Cookie': "",
            'Content-Type': 'application/x-www-form-urlencoded'
        }

    def login(self):
        page = self.page
        page.get('https://jwgl.hrbeu.edu.cn/jwapp/sys/cjcx/*default/index.do?THEME=green&EMAP_LANG=zh#/cjcx')
        login_ele = page.ele('#username')
        login_ele.input(self.username)
        pwd_ele = page.ele('#password')
        pwd_ele.input(self.password)
        captcha_ele = page.ele('@alt=验证码。')
        captcha_src = captcha_ele.attr("src")
        img = captcha_src[captcha_src.find(','):]
        ocr = ddddocr.DdddOcr()
        captcha_result = ocr.classification(img=base64.b64decode(img))
        captcha_input = page.ele('#captcha')
        captcha_input.input(captcha_result)
        login_btn = page.ele('#login-submit')
        login_btn.click()
        time.sleep(10)
        with open("cookie.json", "w", encoding="UTF-8") as f:
            json.dump(page.cookies(all_info=False, as_dict=True), f)

    def getjson(self):
        self.page.close()
        with open("cookie.json", "r", encoding="UTF-8") as f:
            cookies = json.load(f)
        result = [f"{key}={value}" for key, value in cookies.items()]
        for i in result:
            self.headers["Cookie"] = "; ".join(result)
        payload = (
            'querySetting=%5B%7B%22name%22%3A%22SFYX%22%2C%22caption%22%3A%22%E6%98%AF%E5%90%A6%E6%9C%89%E6%95%88%22%2C'
            '%22linkOpt%22%3A%22AND%22%2C%22builderList%22%3A%22cbl_m_List%22%2C%22builder%22%3A%22m_value_equal%22%2C'
            '%22value%22%3A%221%22%2C%22value_display%22%3A%22%E6%98%AF%22%7D%2C%7B%22name%22%3A%22SHOWMAXCJ%22%2C%22caption'
            '%22%3A%22%E6%98%BE%E7%A4%BA%E6%9C%80%E9%AB%98%E6%88%90%E7%BB%A9%22%2C%22linkOpt%22%3A%22AND%22%2C%22builderList'
            '%22%3A%22cbl_m_List%22%2C%22builder%22%3A%22m_value_equal%22%2C%22value%22%3A%220%22%2C%22value_display%22%3A%22'
            '%E5%90%A6%22%7D%5D&*order=-XNXQDM%2C-KCH%2C-KXH'
            '&pageSize=100&pageNumber=1')
        result = requests.post(url="https://jwgl.hrbeu.edu.cn/jwapp/sys/cjcx/modules/cjcx/xscjcx.do",
                               headers=self.headers, data=payload, verify=False)
        with open("result.json", "w", encoding="UTF-8") as f:
            json.dump(result.json(), f, ensure_ascii=False, indent=4)

    def getexcel(self):
        page = self.page
        excel_btn = page.ele("#dqxq-report")
        excel_btn.click()
        page.close()


if __name__ == '__main__':
    jwgl = JWGLWeb("", "")
    jwgl.login()
    jwgl.getexcel()
