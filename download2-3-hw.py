import sys
import io
import urllib.request as req
from urllib.parse import urlencode

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding='utf-8')

imgUrl = "https://ssl.pstatic.net/tveta/libs/1261/1261810/2d1e5170eb5d153f6765_20200103163008965.jpg"
API = "https://nv.veta.naver.com/fxshow"
values = {
  'su' : 'SU10079',
  'calp' : '1',
  'nrefreshx' : '1'
}
#print('before : ', values)

params = urlencode(values)
#print('after : ', params)

url = API + "?" + params
print('요청 url : ', url)

savePath1 = "D:/study/인프런/06.web/004.python/section2/img1.jpg"
savePath2 = "D:/study/인프런/06.web/004.python/section2/hw.gif"

f = req.urlopen(url).read()
f = req.urlopen(imgUrl).read()

with open(savePath1, 'wb') as saveFile1:
    saveFile1.write(f)

print('이미지 저장!')

with open(savePath2, 'wb') as saveFile2 :
    saveFile2.write(f)

print('동영상 저장!')
