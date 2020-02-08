from bs4 import BeautifulSoup
import urllib.request as req
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

url = "https://finance.naver.com/sise/"
res = req.urlopen(url).read().decode('cp949')  # utf-8 : 한글 깨짐, unicode_escape : 한글 깨짐
soup = BeautifulSoup(res, "html.parser")

top10 = soup.select("#siselist_tab_0 > tr")

i = 1
for e in top10:
    if e.find("a") is not None:
        print(i, e.select_one(".tltle").string)
        i += 1
