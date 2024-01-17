class human:
    def __init__(self,name,age,sex):
        self.name = name
        self.age = age
        self.sex = sex

    def who(self):
        print("이름 :{},나이: {},성별:{}".format(self.name,self.age,self.sex))

    def setInfo(self):
        self.name = name
        self.age = age
        self.sex = sex


areum=human("안녕","15","안녕")
areum.who()
