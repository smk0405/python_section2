import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

class UserInfo:
    #메소드 - 객체 초기화시 __init__사용
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone

    def print_info(self):
        print("---------------")
        print("Name: "  + self.name)
        print("Phone: "  + self.phone)
        print("---------------")

    def __del__(self):
        print("삭제가 됩니다")

#인스턴스 : 실제 생성하는 행위. 메모리에 올려지는 객체
user1 = UserInfo("kim", "010-222-4444")
user2 = UserInfo("park", "010-444-5555")

#user1.set_info("kim", "010-222-4444")
#user2.set_info("park", "010-444-5555")

user1.print_info()
user2.print_info()

#인스턴스의 네임스페이스
print(user1.__dict__)
print(user2.__dict__)
