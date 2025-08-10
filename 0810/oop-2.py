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
        if v>30:
            self.exp += 100
        else:
            self.exp += 1
        print(f'你攻擊對手，對方扣{v}HP')
        self.up()

    def up(self):
        if self.exp > 100 + (self.level*10):
            self.exp = 0
            self.level += 1
            print(f'等級提升，目前等級為{self.level}')

hello = User('射手','hello')
print(hello)
print(hello.job)
print(hello.name)
print(hello.hp)
print(hello.mp)
print(hello.exp)
hello.attack(15)
print(hello.exp)
hello.attack(100)
hello.attack(100)
hello.attack(100)
hello.attack(100)
hello.attack(100)
hello.attack(100)
hello.attack(100)
hello.attack(100)
hello.attack(100)
hello.attack(100)
hello.attack(100)
hello.attack(100)
hello.attack(100)
hello.attack(100)

