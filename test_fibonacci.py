#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 20 14:35:09 2020

@author: apple
"""

from fibonacci_p import fib


def test_fib():
    assert fib(0) == 0
    assert fib(1) == 1
    assert fib(10) == 55