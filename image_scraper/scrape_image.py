# -*- coding: utf-8 -*-
"""
Created on Mon Jun 12 15:41:07 2017

@author: pegasus
"""
# requires python3 
# for beautiful soup do
# pip3 install bs4 
import urllib
import bs4 as bs
import os
from urllib import request
from urllib.parse import urljoin
grocery=[
['Lifebuoy+Red+Soap','Lifebuoy+handwash',"lifebuoy+soap"],
['Maggi+noodles','Maggi+noodles+packet',"maggi+small+packet"],
['slice+drink','slice+juice','slice+mango+juice'],
["rin+packet","rin+detergent","rin+washing+powder"],
["chocos+box","kellogg's+chocos","kellogg's+chocos+box"],
["closeup+toothpaste+red","closeup+paste+red","closeup+red+toothpaste"],
["bru+coffee","bru+instant","bru+tea"],
["parleG","ParleG+biscuits","parleg+packet"],
["dairy+milk+fruits+nuts","dairy+milk+chocolate+packet","dairy+milk+chocolate"],
["goodday+butter","goodday+blue+biscuits","goodday+butter+cookies"]
]
# webscraping for grocery items images
# change list to your own

 


for lm in grocery:            
    path='/media/shresth/E486DEEE86DEBFEA/GroceryData/webscraped/'+lm[0]		#can replace with any folder name
    os.mkdir( path)
    i=0
    for gr in lm:
        url='https://www.bing.com/images/search?q='+gr+'&FORM=HDRSC2'
        sauce=urllib.request.urlopen('https://www.bing.com/images/search?q='+gr+'&FORM=HDRSC2').read()
        soup = bs.BeautifulSoup(sauce, 'lxml')
        for img in soup.select("img[src^=http]"):
            i=i+1
            img_url = urljoin(url, img['src'])
            file_name = '/media/shresth/E486DEEE86DEBFEA/GroceryData/webscraped/'+lm[0]+'/'+str(gr)+'_'+str(i)+'.jpg'
            request.urlretrieve(img_url, file_name)
            print(img_url, file_name)
