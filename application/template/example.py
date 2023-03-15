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
    for grade in grade_dict:
        if score < grade_dict[grade]:
            next_grade = grade
            next_grade_point = grade_dict[grade]
        else:
            return f"現在の評価は{grade}です。上位の評価({next_grade})まであと{next_grade_point - score}点です。"


print(next_grade_score(99))  # 現在の評価はSです。上位の評価(S+)まであと1点です。
print(next_grade_score(82))  # 現在の評価はB+です。上位の評価(A)まであと3点です。
print(next_grade_score(71))  # 現在の評価はC+です。上位の評価(B)まであと4点です。
print(next_grade_score(66))  # 現在の評価はCです。上位の評価(C+)まであと4点です。
print(next_grade_score(-15))  # 存在しない点数です。
print(next_grade_score(30.5))  # 存在しない点数です。
print(next_grade_score(100))  # 満点です！素晴らしい！
