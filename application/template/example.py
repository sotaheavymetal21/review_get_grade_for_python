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
    not_exist = "存在しない点数です。"
    if score == 100:
        return "満点です！素晴らしい！"
    if not isinstance(score, int):
        return "存在しない点数です。"
    if score < 0:
        return not_exist
    if score > 100:
        return not_exist
    grade_list = []
    for grade in grade_dict.keys():
        if score >= grade_dict[grade]:
            return f"現在の評価は{grade}です。上位の評価({grade_list[-1]})まであと{grade_dict[grade_list[-1]] - score}点です。"
        else:
            grade_list.append(grade)
