from BeautifulSoup import BeautifulSoup
import pandas as pd
import numpy as np
import mechanize
import requests
import sqlite3
import re



url= 'https://www.youtube.com/feed/trending'


browser = mechanize.Browser()
browser.set_handle_robots(False)
browser.open(url)

response = requests.get(browser.geturl())
html = response.content
soup = BeautifulSoup(html)


linklist = []
ytitles = soup.findAll('a', {'href': re.compile('.*(watch\?v).*')})
for yt in ytitles:
        linklist.append(str(yt['href'])+str(', '))


vtitles = []
for v in vlist:
        urlgo= 'https://www.google.com/#q=youtube.com:+' + re.search('(?<=\=).*', str(v)).group()
        response = requests.get(urlgo)
        html = response.content
        soup = BeautifulSoup(html)
        vtitles.append(str(soup.findAll('a', {'data-href': urlgo})).encode('ascii','ignore').replace('\n', '') + str(', '))
        
        for playerlink in soup.findAll('table', summary=re.compile('Player')):
        a = str(playerlink).encode('ascii','ignore').replace('\n', '')
h3 class r

