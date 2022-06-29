# -*- coding: utf-8 -*-
"""
Created on Wed Jun 15 17:46:58 2022

@author: ghost
"""
import os
import time #how many time takes to load html pages
import requests #download page in html page use for scrapping but beautiful soup is also there
import sys

def retrieve_html():
    for year in range(2013,2019):
        for month in range(1,13):
            if(month <10):
                url = 'https://en.tutiempo.net/climate/0{}-{}/ws-421820.html'.format(month, year)
            else:
                url = 'https://en.tutiempo.net/climate/{}-{}/ws-426470.html'.format(month, year)
        
            texts= requests.get(url)  #import txt from that
            text_utf = texts.text.encode('utf=8') #for support html code
            
            if not os.path.exists('data/html_data/{}'.format(year)):
                os.makedirs('data/html_data/{}'.format(year))
            with open("data/html_data/{}/{}.html".format(year, month), "wb") as output:
                output.write(text_utf)
        
    
        sys.stdout.flush()

if __name__=="__main__":
    start_time = time.time()
    retrieve_html()
    stop_time = time.time()
    print("Time Taken {}".format(stop_time - start_time) )