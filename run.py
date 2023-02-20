#!/usr/bin/env python

import sys
import numpy as np
import pandas as pd
import json
import matplotlib.pyplot as plt

from q2 import level_diff
from q2 import employ_diff
from q2 import type_diff

def main(targets):
    #if 'all' in targets:
        
        
    if 'test' or 'all' in targets:
        df1 = pd.read_json('test/Asian_1.json')
        df2 = pd.read_json('test/Asian_2.json')
        df3 = pd.read_json('test/Asian_3.json')
        df4 = pd.read_json('test/Black_1.json')
        df5 = pd.read_json('test/Black_2.json')
        df6 = pd.read_json('test/Black_3.json')
        df7 = pd.read_json('test/Hispanic_1.json')
        df8 = pd.read_json('test/Hispanic_2.json')
        df9 = pd.read_json('test/Hispanic_3.json')
        df10 = pd.read_json('test/White_1.json')
        df11 = pd.read_json('test/White_2.json')
        df12 = pd.read_json('test/White_3.json')
        df_male = pd.concat([df1,df2,df3,df4,df5,df6,df7,df8,df9,df10,df11,df12], axis=0)
        asian_male = df_male.loc[df_male['ethnicity'] == 'asian']
        hispanic_male = df_male.loc[df_male['ethnicity'] == 'hispanic']
        white_male = df_male.loc[df_male['ethnicity'] == 'white']
        black_male = df_male.loc[df_male['ethnicity'] == 'black']
        
        #plot level differences
        x = np.arange(3)
        y1 = level_diff(asian_male)
        y2 = level_diff(hispanic_male)
        y3 = level_diff(white_male)
        y4 = level_diff(black_male)
        width = 0.2
        plt.bar(x-0.2, y1, width, color='skyblue')
        plt.bar(x, y2, width, color='orange')
        plt.bar(x+0.2, y3, width, color='olivedrab')
        plt.bar(x+0.4, y4, width, color='lightsalmon')
        plt.xticks(x, ['Mid-Senior level', 'Entry level', 'Associate'])
        plt.xlabel("Job Level Difference")
        plt.ylabel("Frequency")
        plt.legend(["Asian", "Hispanic", "White","Black"])
        plt.show() 
        
        #plot number of employee difference
        x = np.arange(8)
        y1 = employ_diff(asian_male)
        y2 = employ_diff(hispanic_male)
        y3 = employ_diff(white_male)
        y4 = employ_diff(black_male)
        width = 0.2
        plt.rcParams["figure.figsize"] = [9.50, 4.50]
        plt.bar(x-0.2, y1, width, color='skyblue')
        plt.bar(x, y2, width, color='orange')
        plt.bar(x+0.2, y3, width, color='olivedrab')
        plt.bar(x+0.4, y4, width, color='lightsalmon')
        plt.xticks(x, ['11-50', '51-200', '201-500','501-1000','1001-5000','5001-10000','10001+','100001+'])
        plt.xlabel("Numbers of Employees ")
        plt.ylabel("Frequency")
        plt.legend(["Asian", "Hispanic", "White","Black"])
        plt.show()
        
        #plot type differences
        types = type_diff(asian_male)[0]
        data = type_diff(asian_male)[1]
        fig = plt.figure(figsize =(9, 5))
        plt.pie(data, labels = types)
        plt.title("Types of Company for Asian Male")
        plt.show()
        types = type_diff(hispanic_male)[0]
        data = type_diff(hispanic_male)[1]
        fig = plt.figure(figsize =(9, 5))
        plt.pie(data, labels = types)
        plt.title("Types of Company for Hispanic Male")
        plt.show()
        types = type_diff(white_male)[0]
        data = type_diff(white_male)[1]
        fig = plt.figure(figsize =(9, 5))
        plt.pie(data, labels = types)
        plt.title("Types of Company for Caucasian Male")
        plt.show()
        types = type_diff(black_male)[0]
        data = type_diff(black_male)[1]
        fig = plt.figure(figsize =(9, 5))
        plt.pie(data, labels = types)
        plt.title("Types of Company for African American Male")
        plt.show()
        
      

if __name__ == '__main__':
    targets = sys.argv[1:]
    main(targets)
    
