import sys
import io
import urllib.request as dw

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding='utf-8')

imgUrl = "http://blogfiles.naver.net/20150922_125/ejdnj119_1442899473477ajKRl_JPEG/%B1%CD%BF%A9%BF%EE%B5%BF%B9%B0003.jpg"
htmlUrl = "http://google.com"

savePath1 = "D:/study/인프런/06.web/004.python/section2/test1.jpg"
savePath2 = "D:/study/인프런/06.web/004.python/section2/index.html"

f = dw.urlopen(imgUrl).read()
f2 = dw.urlopen(htmlUrl).read()

saveFile1 = open(savePath1, 'wb') # w : write, r : read, a : add
saveFile1.write(f)
saveFile1.close()

with open(savePath2, 'wb') as saveFile2: # with문을 쓰면 자동 반납이 됨. close를 명시하지 않아도 됨
    saveFile2.write(f2)




print("다운로드 완료!")
