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

url = "https://www.inflearn.com/"
#url = base + quote

res = req.urlopen(url).read()
savePath = "D:\\study\\인프런\\06.web\\004.python\\section2\\imgDown\\hw\\"

try:
    if not (os.path.isdir(savePath)):
        os.makedirs(os.path.join(savePath))
except OSError as e :
    if e.errno != errno.EEXIST:
        print("폴더 만들기 실패!")
        raise  #에러 강제 발생


#20.01.19 : 인프런 전체 강의 가져오기
soup = BeautifulSoup(res, "html.parser")
main = soup.select("div.course_card_item")
#print(main)


for i, e in enumerate(main, 1):
    with open(savePath+"title_"+str(i)+".txt", "wt") as f :
        f.write(e.select_one("div.course_title").string)
    fullFileName = os.path.join(savePath, savePath+str(i)+'.png')
    req.urlretrieve("https://cdn.inflearn.com/" + rep.quote_plus(e.select_one("figure.is_thumbnail > img")['src'][25:]), fullFileName)

print("인프런 전체 강좌 강의와 이미지 다운 완료!")
