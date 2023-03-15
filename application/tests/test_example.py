#!/usr/bin/env python3
# -*- coding: utf_8 -*-
"""例題プログラム"""
import pytest

from template.example import get_score


def test_S():
    """評価が S のとき"""
    assert get_score(95) == "現在の評価はSです。上位の評価(S+)まであと5点です。"


def test_C():
    """評価が C+ のとき"""
    assert get_score(68) == "現在の評価はCです。上位の評価(C+)まであと2点です。"


def test_E():
    """評価が D のとき"""
    assert get_score(58) == "現在の評価はDです。上位の評価(D+)まであと2点です。"


def test_F():
    """グレードが F のとき"""
    assert get_score(4) == "現在の評価はFです。上位の評価(D)まであと51点です。"


def test_not_exist_point():
    """存在しない点数（100よりも大きい）のとき"""
    assert get_score(105) == "存在しない点数です。"


def test_not_exist_point2():
    """存在しない点数（マイナス）のとき"""
    assert get_score(-15) == "存在しない点数です。"


def test_not_integer():
    """存在しない点数（小数点）のとき"""
    assert get_score(22.5) == "存在しない点数です。"
