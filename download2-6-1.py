from bs4 import BeautifulSoup
import sys
import io
import re #regex

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding='utf-8')

html = """
<html><body>
  <ul>
    <li><a id="naver" href="http://www.naver.com">naver</a></li>
    <li><a href="http://www.daum.net">daum</li>
    <li><a href="https://www.google.com">google</li>
    <li><a href="https://www.tistroy.com">tistory</li>
  </ul>
</body></html>
"""

soup = BeautifulSoup(html, 'html.parser')
#1. a태그 find
#test = soup.find('a', string="naver")
#print(test.string)

#2. id로 find
#print(soup.find(id="naver").string)

#3. 정규표현식으로 find
li = soup.find_all(href=re.compile(r"^https://"))

for ix in li:
  print(ix.attrs['href'])
