from os import environ
import requests
from bs4 import BeautifulSoup
from sys import argv, exit

try:
    proxyDict = {
            'http_proxy': environ['http_proxy'],
            'https_proxy': environ['https_proxy'],
            'ftp_proxy': environ['ftp_proxy'],
            }
except KeyError:
    proxyDict = None

if len(argv) != 2:
    exit('File not specified')

with open(argv[1]) as fle:
    text = fle.read()

title = str(input('Enter the title for the text file: '))

syntaxTab = {
        'txt' : 'text',
        'cpp' : 'cpp',
        'c'   : 'c',
        'html': 'html',
        'css' : 'css',
        'go'  : 'go',
        'py'  : 'python3',
        'php' : 'php',
        'js'  : 'js',
        'java': 'java',
        }

if len(argv[1].split('.')) == 1:
    syn = 'txt'
else:
    syn = argv[1].split('.')[1]

Dat = {
        'poster': title,
        'syntax': syntaxTab[syn],
        'content': text,
        }

r = requests.post('https://paste.ubuntu.com/', data=Dat, proxies=proxyDict)
print(r.text)

soup = BeautifulSoup(r.text, 'lxml')
link = 'http://paste.ubuntu.com/' + soup.find('a').get('href').split('/')[1]
print(link)

