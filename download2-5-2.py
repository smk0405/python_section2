from bs4 import BeautifulSoup
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding='utf-8')

html = """
<html>
<body>
<h1>Python BeautifulSoup 공부</h1>

<p>태그 선택자</p>
<p>css 선택자</p>
</body>
</html>
"""

soup = BeautifulSoup(html, 'html.parser')
#print('soup', type(soup))
#print('prettify', soup.prettify())

h1 = soup.html.body.h1
#print(h1.string)
p1 = soup.html.p
p2 = p1.next_sibling.next_sibling #하나는 엔터공백, 하나가 비로소 태그값
#print('p1', p1)
#print('p2', p2)
p3 = p1.previous_sibling.previous_sibling
#print('p3', p3)

print("h1>>", h1.string)
print("p >>", p1.string)
print("p >>", p2.string)
