#!/usr/bin/env python3
# -*- coding: utf_8 -*-
"""例題プログラム"""


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


def get_score(score_of_test, point = 100):
    list = []
    not_exist = "存在しない点数です。"
    if score_of_test is point:
        return "満点です！素晴らしい！"
    if not isinstance(score_of_test, int):
        return "存在しない点数です。"
    if score_of_test < 0:
        return not_exist
    if score_of_test > 100:
        return not_exist
    for grade in grade_dict.keys():
        if score_of_test >= grade_dict[grade]:
            return f"現在の評価は{grade}です。上位の評価({list[-1]})まであと{grade_dict[list[-1]] - score_of_test}点です。"
        elif score_of_test < grade_dict[grade]:
            list.append(grade)
        else:
            return "点数が存在しません。"
