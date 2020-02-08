from bs4 import BeautifulSoup
import urllib.request as req
import urllib.parse as rep #사용하려는 url에 한글이 있다면 parse 사용해야함
import sys
import io
import os

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

opener = req.build_opener()
opener.addheaders = [('User-agent', 'Mozilla/5.0')]
req.install_opener(opener)

base = "https://search.naver.com/search.naver?where=image&sm=tab_jum&query="
quote = rep.quote_plus("사자")
url = base + quote

res = req.urlopen(url)
savePath = "D:\\study\\인프런\\06.web\\004.python\\section2\\imgDown\\"

try:
    if not (os.path.isdir(savePath)):
        os.makedirs(os.path.join(savePath))
except OSError as e :
    if e.errno != errno.EEXIST:
        print("폴더 만들기 실패!")
        raise  #에러 강제 발생

soup = BeautifulSoup(res, "html.parser")

img_list = soup.select("div.img_area > a.thumb._thumb > img")
#print("Test", img_list)

for i, img_list in enumerate(img_list, 1):
    #print(img_list['data-source'])
    fullFileName = os.path.join(savePath, savePath+str(i)+'.jpg')
    req.urlretrieve(img_list['data-source'], fullFileName)

print("다운로드 완료!")
