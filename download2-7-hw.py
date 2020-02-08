from bs4 import BeautifulSoup
import urllib.request as req
import urllib.parse as rep
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

base = "https://www.daum.net/?t__nil_top=refresh"
res = req.urlopen(base).read()
soup = BeautifulSoup(res, "html.parser")

issue = soup.select("div.hotissue_builtin > div.realtime_part > ol > li > div > div > span.txt_issue")
#print(issue[0].text)
print(issue[0].text)

for top in issue :
    print(top.text)

#for ix, top in enumerate(issue) :
#    print(top[0].text)
