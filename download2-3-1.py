import sys
import io
import urllib.request as req
from urllib.parse import urlparse

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding='utf-8')

url = "http://www.encar.com/index.do"
mem = req.urlopen(url)


#print(type({}))
#print(type([]))
#print(type(()))

#print("geturl : ", mem.geturl())
#print("status : ", mem.status)
#print("headers : ", mem.headers)
#print("info : ", mem.info())
#print("read : ", mem.read(50).decode("utf-8"))

print(urlparse("http://www.encar.com?test=test"))
