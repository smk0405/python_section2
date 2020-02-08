import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

#클래스 변수, 인스턴스 변수

class Warehouse:
    #클래스 변수 : 이건 공유됨
    stock_num = 0
    def __init__(self, name):
        self.name = name
        Warehouse.stock_num += 1

    def __del__(self):
      Warehouse.stock_num -= 1

#user1, user2는 인스턴스 변수 : 이건 공유되지 않음
user1 = Warehouse("kim")
user2 = Warehouse("shin")

print(user1.name)
print(user2.name)
print(user1.__dict__)
print(user2.__dict__)
print(Warehouse.__dict__)

#user1의 네임스페이스를 확인 → 없으면 클래스변수의 네임스페이스를 확인!
print(user1.stock_num)
print(user2.stock_num)
