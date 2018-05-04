import re
import requests
from bs4 import BeautifulSoup
import random
import os

def download_img(data,filename): #Function to download images
    if (os.path.isdir('XKCD')): #Asserts for existence
        pass
    else:
        os.mkdir('XKCD') #If false create a folder
    op_file=open('XKCD/'+filename,'wb')
    op_file.write(data) #Download off
    print "Downloaded",filename


choice=input("How many random images you want to download?? xD \n")


for i in range(choice):
    num = str(random.randint(1,1933))
    url = "http://xkcd.com/"+num+"/"
    r=requests.get(url)
    soup=BeautifulSoup(r.content,'html.parser')  
    filename=str(soup.select('#ctitle')).split('">')
    filename=filename[1].split('<')
    filename=filename[0] #Getting filename using string manip
    img_url=soup.select('#comic')
    img_url=str(img_url).split('src=')[1]
    img_url='https:'+img_url.split('"')[1]
    download_img(requests.get(img_url).content,filename+'.png') #Caling the func i times
