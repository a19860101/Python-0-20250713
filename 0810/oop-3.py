class User:
    def __init__(self, job, name):
        # 屬性
        self.job = job
        self.name = name
        self.hp = 100
        self.mp = 10
        self.exp = 0
        self.level = 1

    def attack(self, v):
        if v > 80: self.exp += 64
        elif v > 60: self.exp += 48
        elif v > 40: self.exp += 32
        elif v > 20: self.exp += 16
        else: self.exp += 8
        print(f'你攻擊對手，對方扣{v}HP')
        print(f'目前經驗值:{self.exp}')
        print('---')
        self.up()

    def up(self):
        if self.exp > 100 + (self.level*10):
            self.exp = self.exp - (100 + (self.level*10))
            self.level += 1
            print(f'等級提升，目前等級為{self.level}')
            print(f'目前經驗值:{self.exp}')
            print('-------------------')
        else:
            print(f'目前等級:{self.level}')
            print('-------------------')


class NPC(User):
    def dead(self):
        print('你已經死了')


qq = NPC('哥布林','林布哥')
# print(qq)

# qq.attack(1)
qq.dead()

u1 = User('射手','John')
u1.dead()