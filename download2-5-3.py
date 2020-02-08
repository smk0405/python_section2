from bs4 import BeautifulSoup
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding='utf-8')

html = """
<html><body>
  <ul>
    <li><a href="http://www.naver.com">naver</a></li>
    <li><a href="http://www.daum.net">daum</li>
    <li><a href="http://www.google.com">google</li>
    <li><a href="http://www.tistroy.com">tistory</li>
  </ul>
</body></html>
"""

soup = BeautifulSoup(html, 'html.parser')

links = soup.find_all("a")
#print('links', type(links))

a = soup.find_all("a", string="daum")
print('a', a)

b = soup.find_all("a", limit=0) #limit=0은 제한 없음을 의미
print('b', b)

c = soup.find_all(string=["naver", "google"])
print('c', c)

for aa in links :
    #print('a', type(a), a)
    href = aa.attrs['href']
    txt = aa.string
    #print('txt >> ', txt, 'href >> ', href)
