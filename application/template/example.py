#!/usr/bin/env python3
# -*- coding: utf_8 -*-
"""例題プログラム"""


def get_grade(score: int) -> str:
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

    for i, (grade, min_score) in enumerate(
        sorted(grade_dict.items(), key=lambda x: -x[1])
    ):
        if score >= min_score:
            if i == 0:
                return "最高評価です！"
            else:
                prev_grade, prev_min_score = sorted(
                    grade_dict.items(), key=lambda x: -x[1]
                )[i - 1]
                return f"{grade}まであと {min_score-score}点です。次の上位は{prev_grade}で、あと{score-prev_min_score}点必要です。"

    return "最低評価です。。。"


print(get_grade(82))  # Aまであと 3点です。次の上位はA+で、あと 8点必要です。
print(get_grade(33))  # Cまであと 2点です。次の上位はC+で、あと 2点必要です。
print(get_grade(2))  # Fまであと 53点です。次の上位はDで、あと 53点必要です。
print(get_grade(0))  # Fまであと 55点です。次の上位はDで、あと 55点必要です。
print(get_grade(33.5))  # Cまであと 1.5点です。次の上位はC+で、あと 1.5点必要です。
print(get_grade(100))  # 最高評価です！
print(get_grade(-10))  # 存在しない点数です。
