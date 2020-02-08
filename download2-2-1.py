import sys
import io
import urllib.request as dw

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding='utf-8')

imgUrl = "http://blogfiles.naver.net/20150922_125/ejdnj119_1442899473477ajKRl_JPEG/%B1%CD%BF%A9%BF%EE%B5%BF%B9%B0003.jpg"
htmlUrl = "http://google.com"

savePath1 = "D:/study/인프런/06.web/004.python/section2/test1.jpg"
savePath2 = "D:/study/인프런/06.web/004.python/section2/index.html"

dw.urlretrieve(imgUrl, savePath1)
dw.urlretrieve(htmlUrl, savePath2)

print("다운로드 완료!")
