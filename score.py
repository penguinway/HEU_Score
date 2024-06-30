import json
import pandas as pd


def cal_by_first():
    with open("result.json", "r", encoding="utf-8") as f:
        result = json.load(f)
    data = result["datas"]["xscjcx"]["rows"]
    course_score = 0  # 总计成绩
    score_sum = 0  # 总计学分
    row = ""
    for course in data:
        if course["KCXZDM_DISPLAY"] == "必修":
            score_sum += course["XF"]
            if course["XSDJCJLXDM_DISPLAY"] == "百分制":
                course_score += course["XF"] * course["ZCJ"]
            if course["XSDJCJLXDM_DISPLAY"] == "五级制":
                if course["XSZCJMC"] == "优秀":
                    course_score += course["XF"] * 95
                if course["XSZCJMC"] == "良好":
                    course_score += course["XF"] * 85
                if course["XSZCJMC"] == "中等":
                    course_score += course["XF"] * 75
                if course["XSZCJMC"] == "及格":
                    course_score += course["XF"] * 65
            print("课程名：", course["XSKCM"], " 学分:", course["XF"], " 成绩:", course["ZCJ"])
            row += "课程名：" + str(course["XSKCM"]) + " 学分:" + str(course["XF"]) + " 成绩:" + str(
                course["ZCJ"]) + '\n'
    print("总学分：", score_sum)
    print("总成绩：", course_score)
    print("平均成绩：", course_score / score_sum)
    row += "总学分：" + str(score_sum) + '\n' + "总成绩：" + str(course_score) + '\n' + "平均成绩：" + str(
        course_score / score_sum)
    with open("result.txt", "w", encoding="utf-8") as f:
        f.write(row)


def cal_by_second():
    data = pd.read_excel("全部成绩查询.xlsx")
    course_score = 0  # 总计成绩
    score_sum = 0  # 总计学分
    row = ""
    for i in range(data.shape[0]):
        if data["课程性质"][i] == "必修":
            print("课程名:", data["课程名"][i], " 学分:", data["学分"][i], " 总成绩:", data["总成绩"][i])
            score_sum += data["学分"][i]
            if data["等级成绩类型"][i] == "百分制":
                course_score += data["学分"][i] * data["总成绩"][i]
            if data["等级成绩类型"][i] == "五级制":
                if data["总成绩"][i] >= 90:
                    course_score += data["学分"][i] * 95
                if data["总成绩"][i] >= 80:
                    course_score += data["学分"][i] * 85
                if data["总成绩"][i] >= 70:
                    course_score += data["学分"][i] * 75
                if data["总成绩"][i] >= 60:
                    course_score += data["学分"][i] * 65
            row += data["课程名"][i] + " " + str(data["学分"][i]) + " " + str(data["总成绩"][i]) + '\n'
    print("总学分：", score_sum)
    print("总成绩：", course_score)
    print("平均成绩：", course_score / score_sum)
    row += "总学分：" + str(score_sum) + '\n' + "总成绩：" + str(course_score) + '\n' + "平均成绩：" + str(
        course_score / score_sum)
    with open("result.txt", "w", encoding="utf-8") as f:
        f.write(row)


if __name__ == '__main__':
    cal_by_second()
