#!/usr/bin/env python3
# -*- coding: utf_8 -*-
"""例題プログラム"""
import pytest

from template.example import next_grade_score


def test_S():
    """グレードが S のとき"""
    assert next_grade_score(95) == "現在の評価はSです。上位の評価(S+)まであと5点です。"


def test_C_plus():
    """グレードが C+ のとき"""
    assert next_grade_score(68) == "現在の評価はCです。上位の評価(C+)まであと2点です。"


def test_when_D():
    """グレードが D のとき"""
    assert next_grade_score(58) == "現在の評価はDです。上位の評価(D+)まであと2点です。"


def test_not_exist_point():
    """存在しない点数（100よりも大きい）のとき"""
    assert next_grade_score(105) == "存在しない点数です。"


def test_not_exist_point2():
    """存在しない点数（マイナス）のとき"""
    assert next_grade_score(-15) == "存在しない点数です。"


def test_not_integer():
    """存在しない点数（小数点）のとき"""
    assert next_grade_score(22.5) == "存在しない点数です。"
