#!/usr/bin/env python3
# -*- coding: utf_8 -*-
"""例題プログラム"""


def get_grade(score):
    grade_dict = {
        "S+": 100,
        "A+": 95,
        "A": 90,
        "B+": 85,
        "B": 80,
        "C+": 75,
        "C": 70,
        "D+": 65,
        "D": 60,
        "F+": 55,
        "F": 0,
    }

    if score < 0 or score > 100:
        return "Score is out of range"

    for key in sorted(grade_dict.keys(), reverse=True):
        if score >= grade_dict[key]:
            return key

    return "Score is out of range"


print(get_grade(99))
print(get_grade(85))
print(get_grade(30))
print(get_grade(100))
print(get_grade(110))
print(get_grade(-10))
