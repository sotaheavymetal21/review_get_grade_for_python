#!/usr/bin/env python3
# -*- coding: utf_8 -*-
"""実行スクリプト
"""

from template.example import next_grade_score

if __name__ == "__main__":
    print(next_grade_score(95))  # 現在の評価はSです。上位の評価(S+)まであと5点です。
    print(next_grade_score(68))  # 現在の評価はCです。上位の評価(C+)まであと2点です。
    print(next_grade_score(58))  # 現在の評価はDです。上位の評価(D+)まであと2点です。
    print(next_grade_score(105))  # 現在の評価はCです。上位の評価(C+)まであと4点です。
    print(next_grade_score(-15))  # 存在しない点数です。
    print(next_grade_score(22.5))  # 存在しない点数です。
    print(next_grade_score(100))  # 満点です！素晴らしい！
