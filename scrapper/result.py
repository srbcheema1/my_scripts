from os import environ
import requests
from bs4 import BeautifulSoup
from sys import argv, exit

class Student:
    #set base year as current year
    base_year = 17
    try:
        proxyDict = {
                    'http_proxy': environ['http_proxy'],
                    'https_proxy': environ['https_proxy'],
                    'ftp_proxy': environ['ftp_proxy']
                }
    except KeyError:
        proxyDict = None

    def __init__(self,num):
        num = str(num)
        self.year = num[0:2]
        if(num[2]=='m' or num[2]=='M'):
            self.branch=num[2:4].lower()
            self.branch+=str(num[4])
            self.roll=num[5:7]
        else:
            self.branch=num[2]
            self.roll=num[3:5]
        self.lastsem = (Student.base_year-int(self.year))*2
        self.rollno = self.year+self.branch+self.roll
        try:         
            url = "http://14.139.56.15/scheme"+self.year+"/studentresult/details.asp"
            page = requests.post(url,data={'RollNumber':self.rollno},proxies=Student.proxyDict,verify=False)        
            soup = BeautifulSoup(page.text,'lxml')
            self.all_data = soup.find_all(class_='ewTable')
            self.name=self.all_data[0].find_all('tr')[0].find_all('td')[1].text.strip()
            res = self.all_data[self.lastsem*2].find_all('tr')[1].find_all('td')
            self.sgpa = res[0].text.strip().split("=")[1]
            cgpa_ = res[2].text.strip()
            self.points = cgpa_.split("/")[0]
            self.cgpa = cgpa_.split("=")[1]
        except:
            self.name = '-'
            self.sgpa = self.points = self.cgpa = '0'

    def display_result(self):
        out = self.name + "\n\t" + self.sgpa + "\n\t" +self.points+ "\n\t" + self.cgpa
        return out

if(len(argv)==2):
    roll=argv[1]
else:
    print("enter ur roll : ",end='')
    roll = str(input())

std = Student(roll)

print(std.display_result())

def sort_std(std):
    return float(std.sgpa)

print("do you want relult of whole class y or n : ",end='')
data=[]
ans = input()
if(ans!='y'):
    exit()
print("enter roll number except last 2 digits ex \'15mi5\' : ",end='')
temp = input()
print("enter range of roll numbers : ",end='')
a , b = input().split(' ')
a = int(a)
b = int(b)
if(ans=='y'):
    for i in range(a,b):
        roll = temp
        roll += "%02d"%(i)
        std = Student(roll)
        if(std.name!='0'):
            data.append(std)
            print(std.display_result())
            print()
    data.sort(key=sort_std,reverse=True)
    print("sorting....\n\n\n")
    for item in data:
        print(item.display_result())
        print()

