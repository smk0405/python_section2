import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')


class NameTest:
    total = 0

print(dir()) #문서의 네임스페이스
print("before: " , NameTest.__dict__)
NameTest.total = 1;
print("after: " , NameTest.__dict__)

n1 = NameTest()
n2 = NameTest()
print(id(n1), " vs ", id(n2))
print(dir())

print(n1.__dict__)
n1.total = 333;
print(n2.__dict__)
print(n1.__dict__)

print(n1.total) #n1은 본인의 네임스페이스에서 값을 출력
print(n2.total) #n2의 네임스페이스에는 total이라는 없기에 클래스변수에 있는 것을 출력
