#!/usr/bin/env python3
# -*- coding: utf_8 -*-
"""例題プログラム"""


def next_grade_score(score):
    grade_dict = {
        "S+": 100,
        "S": 95,
        "A+": 90,
        "A": 85,
        "B+": 80,
        "B": 75,
        "C+": 70,
        "C": 65,
        "D+": 60,
        "D": 55,
        "F": 0,
    }
    if score == 100:
        return "満点です！素晴らしい！"
    if score < 0 or score > 100 or not isinstance(score, int):
        return "存在しない点数です。"
    grade_list = []
    for grade, point in grade_dict.items():
        if score > point:
            return f"現在の評価は{grade}です。上位の評価({grade_list[-1]})まであと{grade_dict[grade_list[-1]] - score}点です。"
        else:
            grade_list.append(grade)


print(next_grade_score(99))  # 上位の評価S+まであと1点です。
print(next_grade_score(82))  # 上位の評価Aまであと3点です。
print(next_grade_score(71))  # 上位の評価Bまであと4点です。
print(next_grade_score(66))  # 上位の評価C+まであと4点です。
print(next_grade_score(-15))  # 存在しない点数です。
print(next_grade_score(30.5))  # 上位の評価Dまであと24.5点です。
print(next_grade_score(100))  # 上位の評価S+まであと0点です。

#    for grade in grade_dict.keys():
#       if score > grade_dict[grade]:
#          return f"現在の評価は{grade}です。上位の評価({grade_list[-1]})まであと{grade_dict[grade_list[-1]] - score}点です。"
#     else:
#        grade_list.append(grade)
