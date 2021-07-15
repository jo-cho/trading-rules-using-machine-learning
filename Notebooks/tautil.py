# -*- coding: utf-8 -*-
"""
Created on Mon Mar  1 23:18:11 2021

@author: JHCho
"""
import pandas as pd
import numpy as np
import ta

def get_rsi(close,window=20):
    rsi = ta.momentum.rsi(close,window)
    return rsi
    
def my_rsi(close, window=20, threshold=66, binary=False):
    rsi = get_rsi(close, window)
    rsi_ = rsi.copy()

    # predict downtrend (overbought --> mean-reverse)
    mrdown2 = (rsi>=80)
    mrdown1 = (rsi<80) & (rsi>=threshold)

    # predict uptrend (oversold --> mean-reverse)
    mrup2 = (rsi<=20)
    mrup1 = (rsi>20) & (rsi<=(100-threshold))

    # predict uptrend (momentum effect)
    tfup3 = (rsi>50) & (rsi<=55)
    tfup2 = (rsi>55) & (rsi<=60)
    tfup1 = (rsi>60) & (rsi<=threshold)

    # predict downtrend (momentum effect)
    tfdown3 = (rsi>45) & (rsi<=50)
    tfdown2 = (rsi>40) & (rsi<=45)
    tfdown1 = (rsi>(100-threshold)) & (rsi<=40)

    if binary is False:
            rsi_.loc[mrdown2] = -2
            rsi_.loc[mrdown1] = -1
            rsi_.loc[mrup2] = 2
            rsi_.loc[mrup1] = 1
            rsi_.loc[tfdown3] = -3
            rsi_.loc[tfdown2] = -2
            rsi_.loc[tfdown1] = -1
            rsi_.loc[tfup3] = 3
            rsi_.loc[tfup2] = 2
            rsi_.loc[tfup1] = 1
    else:
            rsi_.loc[mrdown2] = -1
            rsi_.loc[mrdown1] = -1
            rsi_.loc[mrup2] = 1
            rsi_.loc[mrup1] = 1
            rsi_.loc[tfdown3] = -1
            rsi_.loc[tfdown2] = -1
            rsi_.loc[tfdown1] = -1
            rsi_.loc[tfup3] = 1
            rsi_.loc[tfup2] = 1
            rsi_.loc[tfup1] = 1
    rsi_.dropna(inplace=True)
    return rsi_

def my_rsi_2(close, window=20):
    rsi = get_rsi(close, window)
    rsi_ = rsi.copy()

    # predict downtrend (overbought --> mean-reverse)
    mrdown = (rsi>75)

    # predict uptrend (oversold --> mean-reverse)
    mrup = (rsi>1) & (rsi<32)

    # predict uptrend (momentum effect)
    tfup = (rsi>=55) & (rsi<=66)

    # predict downtrend (momentum effect)
    tfdown = (rsi>33) & (rsi<=45)

    rsi_.loc[mrdown] = -1
    rsi_.loc[mrup] = 1
    rsi_.loc[tfdown] = -1
    rsi_.loc[tfup] = 1
    
    rsi_.dropna(inplace=True)
    rsi_=rsi_.loc[rsi_<2]
    return rsi_