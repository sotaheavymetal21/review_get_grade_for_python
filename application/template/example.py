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

    if score < 0 or score > 100:
        return "存在しない点数です。"

    for index, key in enumerate(sorted(grade_dict.keys(), reverse=True)):
        print(index, key, grade_dict[key])

    return "いうことはありません。素晴らしい！"


print(next_grade_score(82))  # Sまであと 8点です。
print(next_grade_score(33))  # Cまであと 37点です。
print(next_grade_score(2))  # Fまであと 53点です。
print(next_grade_score(0))  # Fまであと 55点です。
print(next_grade_score(33.5))  # Cまであと 31.5点です。
print(next_grade_score(100))  # いうことはありません。素晴らしい！
print(next_grade_score(-10))  # 存在しない点数です。
