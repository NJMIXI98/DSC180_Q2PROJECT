#!/usr/bin/env python

import sys
import json
import matplotlib.pyplot as plt

from q2 import get_data
from q2 import average_price
from q2 import model
from q2 import plot
from q2 import create_ranks
from q2 import rank_plot
from q2 import price_row
from q2 import price
from q2 import locate

def main(targets):
    if 'all' in targets:
        print("I put raw data in google drive!")
        
    if 'test' in targets:
        df = get_data('test/test.json')
        a= average_price(df)
        print(a)
        b= model(df)
        print(b)
        print(model(df[df.scraper == 'Realtor']))
        print(model(df[df.scraper == 'Trulia']))
        print(plot(df))
        plot(df)
        plt.show(block=False)
        gender_ranks = create_ranks(df,'gender')
        race_ranks = create_ranks(df,'ethnicity')
        print(rank_plot(gender_ranks))
        print(rank_plot(race_ranks))
        rank_plot(gender_ranks)
        rank_plot(race_ranks)
        plt.xlabel('Ranking')
        plt.ylabel('Average Price')
        plt.show(block=False)
      

if __name__ == '__main__':
    targets = sys.argv[1:]
    main(targets)
    
