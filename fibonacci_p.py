#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 20 14:33:21 2020

@author: apple
"""

def fib(n):
    old, new = 0, 1
    for _ in range(n):
        old, new = new, old + new
    return old