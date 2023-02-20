#!/usr/bin/env python
# coding: utf-8


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def level_diff(df):
    mid = (df.loc['level'].values == "Mid-Senior level").sum()
    entry = (df.loc['level'].values == "Entry level").sum()
    asso = (df.loc['level'].values == "Associate").sum()
    return [mid,entry,asso]

def employ_diff(df):
    a = (df.loc['employees'].values == "11-50").sum()
    b = (df.loc['employees'].values == "51-200").sum()
    c = (df.loc['employees'].values == "201-500").sum()
    d = (df.loc['employees'].values == "501-1000").sum()
    e = (df.loc['employees'].values == "1001-5000").sum()
    f = (df.loc['employees'].values == "5001-10000").sum()
    g = (df.loc['employees'].values == "10001+").sum()
    h = (df.loc['employees'].values == "100001+").sum()
    return [a,b,c,d,e,f,g,h]


def type_diff(df):
    types = ['IT Services and IT Consulting', 'Technology, Information and Internet', 'Software Development','Data Infrastructure and Analytics',
               'Advertising Services','Financial Services','Non-profit Organizations','Human Resources Services']
    names = []
    count = []
    for i in types:
        data = (df.loc['type'].values == i).sum()
        if data != 0:
            names.append(i)
            count.append(data)
    return names,count





