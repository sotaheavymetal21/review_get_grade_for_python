#!/usr/bin/env python3
# -*- coding: utf_8 -*-
"""例題プログラム"""

from template.example import next_grade_score


def test_1():
    """グレードが S のとき"""
    assert next_grade_score(95) == "現在の評価はSです。上位の評価(S+)まであと5点です。"


def test_2():
    """グレードが C+ のとき"""
    assert next_grade_score(68) == "現在の評価はC+です。上位の評価(B)まであと7点です。"

def test_3():
    """グレードが D のとき"""
    assert next_grade_score(58) == "現在の評価はDです。上位の評価(D+)まであと2点です。"


def test_4():
    """存在しない点数（100よりも大きい）のとき"""
    assert next_grade_score(105) == "存在しない点数です。"


def test_5():
    """存在しない点数（マイナス）のとき"""
    assert next_grade_score(-15) == "存在しない点数です。"


def test_6():
    """存在しない点数（小数点）のとき"""
    assert next_grade_score(22.5) == "存在しない点数です。"
