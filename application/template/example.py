#!/usr/bin/env python3
# -*- coding: utf_8 -*-
"""例題プログラム"""


def next_grade_score(score):
    """
    点数を受け取り、該当する評価と上位の評価までの差分を返す

    Args:
    score (int): ユーザーのテストの得点。範囲は0~100
    Returns:
    str: 現在の評価と上位の評価までの差分を返す
        与えられたscoreが100の場合、'満点です！素晴らしい！'と返す
        与えられたscoreが0~100以外の整数である場合、'存在しない点数です。'と返す
        与えられたscoreが評価表に含まれている場合、現在の評価と上位の評価までの差分を返す
    """
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
